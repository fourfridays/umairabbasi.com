from .models import NodeSnippetViewSet
from wagtail.snippets.models import register_snippet

register_snippet(NodeSnippetViewSet)