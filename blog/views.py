from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render_to_response, get_object_or_404

from wagtail.wagtailcore.models import Page

from .models import BlogIndexPage, BlogPage

def posts(request):
	posts = BlogPage.objects.all().filter(date__lte=timezone.now()).order_by('-date')
	return render(request, 'blog/blog_index_page.html', {'posts': posts})