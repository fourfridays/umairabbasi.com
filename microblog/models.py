from __future__ import unicode_literals
from operator import attrgetter

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.blocks import DateTimeBlock, RichTextBlock
from wagtail.fields import StreamField
from wagtail.models import Page, Orderable

from taxonomy.models import Node


class MicroBlogPeopleRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `People` within the `base`
    app and the BlogPage below. This allows People to be added to a BlogPage.

    We have created a two way relationship between BlogPage and People using
    the ParentalKey and ForeignKey
    """

    page = ParentalKey(
        "MicroBlogPage",
        related_name="micro_blog_person_relationship",
        on_delete=models.CASCADE,
    )
    people = models.ForeignKey(
        "page.People",
        related_name="person_micro_blog_relationship",
        on_delete=models.CASCADE,
    )
    panels = [FieldPanel("people")]


class MicroBlogPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the MicroBlogPage object and tags. There's a longer guide on using it at
    http://docs.wagtail.io/en/latest/reference/pages/model_recipes.html#tagging
    """

    content_object = ParentalKey(
        "MicroBlogPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class MicroBlogPage(Page):
    """
    A MicroBlog Page

    We access the People object with an inline panel that references the
    ParentalKey's related_name in BlogPeopleRelationship. More docs:
    http://docs.wagtail.io/en/latest/topics/pages.html#inline-models
    """

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField(
        [
            (
                "paragraph",
                RichTextBlock(
                    features=["h2", "h3", "bold", "italic", "link", "code"],
                    icon="pilcrow",
                    template="blocks/paragraph_block.html",
                ),
            ),
            (
                "date_published",
                DateTimeBlock(blank=True, null=True),
            ),
        ],
        use_json_field=True,
    )
    tags = ClusterTaggableManager(through=MicroBlogPageTag, blank=True)
    category = models.ForeignKey(
        "taxonomy.Node",
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        limit_choices_to=Node.get_micro_blog_categories,
        default="",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("body"),
        InlinePanel(
            "micro_blog_person_relationship", label="Author(s)", panels=None, min_num=1
        ),
        FieldPanel("tags"),
        FieldPanel("category"),
    ]

    def authors(self):
        """
        Returns the BlogPage's related People. Again note that we are using
        the ParentalKey's related_name from the BlogPeopleRelationship model
        to access these objects. This allows us to access the People objects
        with a loop on the template. If we tried to access the blog_person_
        relationship directly we'd print `blog.BlogPeopleRelationship.None`
        """
        authors = [n.people for n in self.micro_blog_person_relationship.all()]
        return authors

    def get_context(self, request):
        context = super(MicroBlogPage, self).get_context(request)
        context["tags"] = self.tags.all().order_by("name")
        return context

    # Specifies parent to BlogPage as being BlogIndexPages
    parent_page_types = ["MicroBlogIndexPage"]

    # Specifies what content types can exist as children of BlogPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


class MicroBlogIndexPage(RoutablePageMixin, Page):
    """
    Index page for MicroBlogs.
    We need to alter the page model's context to return the child page objects,
    the BlogPage objects, so that it works as an index page

    RoutablePageMixin is used to allow for a custom sub-URL for the tag views
    defined above.
    """

    introduction = models.TextField(help_text="Text to describe the page", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction", classname="full"),
    ]

    # Speficies that only MicroBlogPage objects can live under this index page
    subpage_types = ["MicroBlogPage"]

    # Defines a method to access the children of the microblog page
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super().get_context(request)
        posts = MicroBlogPage.objects.descendant_of(self).live()

        # Extract date_published from each post's StreamField
        for post in posts:
            for block in post.body:
                if block.block_type == 'date_published':
                    post.date_published = block.value
                    break

        # Sort posts by date_published
        context['posts'] = sorted(posts, key=attrgetter('date_published'), reverse=True)

        return context

    # This defines a Custom view that utilizes Tags. This view will return all
    # related BlogPages for a given Tag or redirect back to the BlogIndexPage.
    # More information on RoutablePages is at
    # http://docs.wagtail.io/en/latest/reference/contrib/routablepage.html
    @route(r"^tag/$")
    def all_micro_blog_tags(self, request):
        tags = MicroBlogPageTag.objects.all().order_by("tag__name")
        context = {"tags": tags}
        return render(request, "tags/micro_blog_tags_index_page.html", context)

    @route(r"^tag/([\w-]+)/$")
    def tag_archive(self, request, tag=None):
        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no articles tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        posts = self.get_posts(tag=tag)
        context = {"tag": tag, "posts": posts}
        return render(request, "tags/blog_tag_index_page.html", context)

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child BlogPage objects for this BlogPageIndex.
    # If a tag is used then it will filter the posts by tag.
    def get_posts(self, tag=None):
        posts = MicroBlogPage.objects.live().descendant_of(self)
        if tag:
            posts = posts.filter(tags=tag)
        return posts

    # Returns the list of Tags for all child posts of this BlogPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_posts():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags
