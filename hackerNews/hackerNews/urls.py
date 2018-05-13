from django.contrib import admin
from django.urls import path

urlpatterns = [
    path(r'^$', 'djangorocks.blog.views.index'),
	path(r'^blog/view/(?P<slug>[^\.]+).html', 'djangorocks.blog.views.view_post', name='view_blog_post'),
	path(r'^blog/category/(?P<slug>[^\.]+).html', 'djangorocks.blog.views.view_category', name='view_blog_category'),
]
