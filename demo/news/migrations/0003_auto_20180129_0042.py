# Generated by Django 2.0.1 on 2018-01-29 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newscomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newscomment',
            old_name='news',
            new_name='news_id',
        ),
    ]
