from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100, default="New Tittle")
    body = models.TextField(default="No text")
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    pubdate = models.DateField(auto_now_add=True)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    # Metadata
    class Meta: 
        ordering = ["-pubdate"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('home', args=[str(self.id)])
