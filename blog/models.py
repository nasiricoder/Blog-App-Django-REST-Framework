from typing import Iterable
from django.contrib import admin
from django.conf import settings
from django.db import models
from django.urls import reverse
# from .validators import validate_file_size


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
        ordering = ['-title']
        indexes = [models.Index(fields=['title'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Author")
        verbose_name_plural = ("Authors")
        ordering = [
            'user__first_name', 'user__last_name'
        ]

    def get_absolute_url(self):
        return reverse("Author_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(
        max_length=255, unique=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='blog_post')
    body = models.TextField()
    image = models.ImageField(
        upload_to='blog/images', blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='posts')

    class Meta:
        verbose_name = ('Post')
        verbose_name_plural = ('Posts')
        ordering = ['-published_date']
        unique_together = ['title', 'slug']
        indexes = [
            models.Index(
                fields=['published_date']
            )
        ]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='blog_comment')
    body = models.TextField(unique=True)
    published_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        verbose_name = ('Comment')
        verbose_name_plural = ('Comments')
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['published_date'])
        ]

    def __str__(self):
        return f'Comment by {self.author.user.username}'
