from django.contrib import admin
from django.urls import path
from blog import views
from django.conf.urls import include

urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
	path('admin/', admin.site.urls),
    path(r'', views.index, name='home'),
    path(r'register/', views.register_user, name='register_user'),
	path(r'new_article/', views.new_article, name='new_article'),
	path(r'<int:pk>', views.article, name='view_article'),	
	path(r'<int:pk>/comments', views.comments, name='comments'),
	path(r'<int:pk>/vote', views.vote, name='vote'),
]
