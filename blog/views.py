from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .filters import PostFilter
from .models import Post, Category, Comment, Author
from .serializers import PostSerializer, CommentSerializer, CategorySerializer, AuthorSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.annotate(comments_id=Count('comments'))
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['category__title']
    ordering_fields = ['published_date']


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {
            'post_id': self.kwargs['post_pk']
        }

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
