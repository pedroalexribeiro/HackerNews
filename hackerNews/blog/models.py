from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, default="New Title")
    link = models.URLField()
    pubdate = models.DateTimeField(auto_now_add=True)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    visible = models.BooleanField(default=True)
    upvote = models.BooleanField(default=False)

    # Metadata
    class Meta: 
        ordering = ["-pubdate"]
        permissions = (("can_change_status", "Can see and change articles"),)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_article', args=[str(self.id)])

class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL, related_name="comments")
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])

class Vote(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL, related_name='votes')
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.person.username
