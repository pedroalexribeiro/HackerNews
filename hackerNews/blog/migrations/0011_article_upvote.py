# Generated by Django 2.0.2 on 2018-05-16 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='upvote',
            field=models.BooleanField(default=False),
        ),
    ]
