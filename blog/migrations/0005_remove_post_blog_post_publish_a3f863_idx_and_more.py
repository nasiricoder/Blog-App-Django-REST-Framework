# Generated by Django 5.0.3 on 2024-03-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='post',
            name='blog_post_publish_a3f863_idx',
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255, unique=True), max_length=255, unique_for_date='published_date'),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('title', 'slug')},
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['published_date'], name='blog_post_publish_205817_idx'),
        ),
    ]