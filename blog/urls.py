from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.posts),
	url(r'^(?P<slug>[-\w\d]+)/$', views.post),
]