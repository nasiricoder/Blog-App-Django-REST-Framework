# Generated by Django 5.0.3 on 2024-03-23 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='djangodbmodelsfieldscharfield', max_length=255, unique=True),
        ),
    ]
