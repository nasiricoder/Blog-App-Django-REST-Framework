from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.contenttypes.admin import GenericTabularInline
from blog.admin import PostAdmin
from blog.models import Post
from likes.models import LikedItem
from tags.models import Tag, TaggedItem
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide', 'extrapretty'),
            'fields': [('first_name', 'last_name'), 'username', 'password1', 'password2', 'email']
        }),
    )
    search_fields = ['username']


class TaggdItemInline(GenericTabularInline):
    model = TaggedItem


class CustomPostAdmin(PostAdmin):
    inlines = [TaggdItemInline]


admin.site.unregister(Post)
admin.site.register(Post, CustomPostAdmin)
