from rest_framework import serializers
from .models import Post, Category, Comment, Author


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'body',
                  'published_date', 'image', 'last_modified', 'category', 'status']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'body',
                  'published_date', 'last_modified']

    def create(self, validated_data):
        return Comment.objects.create(post_id=self.context['post_id'], **validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'user', 'phone', 'birth_date', 'address']
