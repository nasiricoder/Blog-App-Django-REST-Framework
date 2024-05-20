from django.contrib import admin
from django.db.models import Count, QuerySet
# from django.utils.translation import gettext_lazy as _
from django.http import HttpRequest
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode
import datetime
from typing import Any
from .models import Post, Author, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['title', 'post_count']
    search_fields = ['title']

    def post_count(self, category: Category):
        url = (reverse('admin:blog_post_changelist')
               + '?'
               + urlencode({'category_id': str(category.id)}))

        return format_html(f'<a href="{url}">{category.posts.count()}</a>')

    def get_queryset(self, request: HttpRequest):
        return super().get_queryset(request).annotate(blog_count=Count('posts'))


class PostCommentInline(admin.TabularInline):
    model = Comment
    autocomplete_fields = ['post']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    actions = ['upbody']
    prepopulated_fields = {
        'slug': ['title']
    }
    search_fields = ['title', 'published_date']
    list_display = ['title', 'author', 'body',
                    'category', 'published_date', 'status', 'image', 'comment_count']
    list_editable = ['status']
    list_per_page = 10
    inlines = [PostCommentInline]
    date_hierarchy = 'published_date'
    autocomplete_fields = ['category', 'author']
    list_select_related = ['category', 'author']
    ordering = ['title', 'author']

    @admin.display(ordering='published_date')
    def comment_count(self, post: Post):
        return post.comments.count()

    @admin.action(description='update body of post')
    def upbody(self, request, queryset: QuerySet):
        upbody = queryset.update(body='Your Hacked!')
        self.message_user(request, message=f'{
                          upbody} posts were updated.')


class BirthdayFilter(admin.SimpleListFilter):
    parameter_name = 'decade'
    title = 'birthday'

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        return [
            ('90s', 'in the nineties'),
            ('80s', 'in the eighties'),
        ]

    def queryset(self, request: Any, queryset: QuerySet[Any]) -> QuerySet[Any] | None:
        if self.value() == '80s':
            return queryset.filter(birth_date__gte=datetime.date(1980, 1, 1), birth_date__lte=datetime.date(1980, 12, 29))
        elif self.value() == '90s':
            return queryset.filter(birth_date__gte=datetime.date(1990, 1, 1), birth_date__lte=datetime.date(1999, 12, 29))


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    model = Author
    list_display = ['phone', 'user', 'birth_date', 'address', 'author_mail']
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['user']
    list_filter = [BirthdayFilter]
    autocomplete_fields = ['user']
    list_select_related = ['user']

    def author_mail(self, author: Author):
        return author.user.email


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ['author', 'post',
                    'published_date', 'last_modified', 'body']
    autocomplete_fields = ['author', 'post']
