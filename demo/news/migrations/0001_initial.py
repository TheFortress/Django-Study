# Generated by Django 2.0.1 on 2018-01-28 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('body', models.TextField()),
                ('photo', models.FileField(upload_to='news/')),
            ],
        ),
    ]
