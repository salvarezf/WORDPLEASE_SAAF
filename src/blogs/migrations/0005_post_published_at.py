# Generated by Django 2.0 on 2018-01-12 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_remove_post_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
