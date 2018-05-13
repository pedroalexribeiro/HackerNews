from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path(r'', views.index, name='index'),
	path(r'blog/view/', views.view_post, name='view_blog_post'),
	path(r'blog/category/', views.view_category, name='view_blog_category'),
]
