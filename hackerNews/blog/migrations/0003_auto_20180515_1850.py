# Generated by Django 2.0.2 on 2018-05-15 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180515_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
