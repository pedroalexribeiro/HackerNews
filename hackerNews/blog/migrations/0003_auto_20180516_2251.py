# Generated by Django 2.0.2 on 2018-05-16 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180516_2250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['pubdate'], 'permissions': (('can_change_status', 'Can see and change articles'),)},
        ),
    ]
