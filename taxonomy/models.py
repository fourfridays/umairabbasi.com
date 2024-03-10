"""Node model and Node admin interaction."""

from django import forms
from django.urls import re_path
from django.core.exceptions import PermissionDenied
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.template.loader import render_to_string

from treebeard.mp_tree import MP_Node

from wagtail.admin.panels import FieldPanel
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.snippets.views.snippets import SnippetViewSet


node_name_validator = RegexValidator(
    regex="^[\w][a-zA-Z &]+$",
    message="Letters, numbers and '&' only plus must start with a letter.",
)


class Node(MP_Node):
    """Represents a single nestable Node in the corporate taxonomy."""

    # node editable fields
    name = models.CharField(
        max_length=80,
        unique=True,
        help_text="Keep the name short, ideally one word.",
        validators=[node_name_validator, MinLengthValidator(4)],
    )
    aliases = models.TextField(
        "Also known as",
        max_length=255,
        blank=True,
        help_text="What else is this known as or referred to as?",
    )

    # node tree specific fields and attributes
    node_order_index = models.IntegerField(
        blank=True,
        default=0,
        editable=False
    )
    node_child_verbose_name = "child"
    node_order_by = ["node_order_index", "name"]

    panels = [
        # FieldPanel('parent'),  # virtual field - see TaxonomyForm
        FieldPanel("name"),
        FieldPanel("aliases", widget=forms.Textarea(attrs={"rows": "5"})),
    ]

    def get_as_listing_header(self):
        """Build HTML representation of node with title & depth indication."""
        depth = self.get_depth()
        rendered = render_to_string(
            "includes/node_list_header.html",
            {
                "depth": depth,
                "depth_minus_1": depth - 1,
                "is_root": self.is_root(),
                "name": self.name,
            },
        )
        return rendered

    get_as_listing_header.short_description = "Name"
    get_as_listing_header.admin_order_field = "name"

    def get_parent(self, *args, **kwargs):
        """Duplicate of get_parent from treebeard API."""
        return super().get_parent(*args, **kwargs)

    get_parent.short_description = "Parent"

    def delete(self):
        """Prevent users from deleting the root node."""
        if self.is_root():
            raise PermissionDenied("Cannot delete root Taxonomy.")
        else:
            super().delete()

    def get_blog_categories():
        return {
            "pk__in": Node.objects.get(name="Blog")
            .get_children()
            .values_list("id", flat=True)
        }
    
    def get_micro_blog_categories():
        return {
            "pk__in": Node.objects.get(name="Blog")
            .get_children()
            .values_list("id", flat=True)
        }

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Taxonomy"
        verbose_name_plural = "Taxonomies"


class BasicNodeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        depth_line = "-" * (obj.get_depth() - 1)
        return "{} {}".format(depth_line, super().label_from_instance(obj))


class NodeForm(WagtailAdminModelForm):

    parent = BasicNodeChoiceField(
        required=True,
        queryset=Node.objects.all(),
        empty_label=None,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs["instance"]

        if instance.is_root() or Node.objects.count() == 0:
            # hide and disable the parent field
            self.fields["parent"].disabled = True
            self.fields["parent"].required = False
            self.fields["parent"].empty_label = "N/A - Root Node"
            self.fields["parent"].widget = forms.HiddenInput()

            # update label to indicate this is the root
            self.fields["name"].label += " (Root)"
        elif instance.id:
            self.fields["parent"].initial = instance.get_parent()

    def save(self, commit=True, *args, **kwargs):
        instance = super().save(commit=False, *args, **kwargs)
        parent = self.cleaned_data["parent"]

        if not commit:
            # simply return the instance if not actually saving (committing)
            return instance

        if instance.id is None:  # creating a new node
            if Node.objects.all().count() == 0:  # no nodes, creating root
                Node.add_root(instance=instance)  # add a NEW root node
            else:  # nodes exist, must be adding node under a parent
                instance = parent.add_child(instance=instance)
        else:  # editing an existing node
            instance.save()  # update existing node
            if instance.get_parent() != parent:
                instance.move(parent, pos="sorted-child")
        return instance


Node.base_form_class = NodeForm

class NodeSnippetViewSet(SnippetViewSet):
    """Class for presenting taxonomies in admin using modeladmin."""

    model = Node

    # admin menu options
    icon = "fa-cube"  # using wagtail fontawesome
    menu_order = 800

    # listing view options
    list_display = ("get_as_listing_header", "get_parent", "aliases")
    list_per_page = 50
    search_fields = ("name", "aliases")

    # inspect view options
    inspect_view_enabled = True
    inspect_view_fields = ("name", "get_parent", "aliases", "id")

    def get_admin_urls_for_registration(self):
        """Add the new url for add child page to the registered URLs."""
        urls = super().get_admin_urls_for_registration()
        add_child_url = re_path(
            self.url_helper.get_action_url_pattern("add_child"),
            self.add_child_view,
            name=self.url_helper.get_action_url_name("add_child"),
        )
        return urls + (add_child_url,)
