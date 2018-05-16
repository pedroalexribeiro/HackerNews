from django.contrib import admin
from .models import Article, Comment, Vote

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('pubdate',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Vote)