from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register(prefix='posts', viewset=views.PostViewSet)
router.register(prefix='categories', viewset=views.CategoryViewSet)
router.register(prefix='authors', viewset=views.AuthorViewSet)

posts_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
posts_router.register('comments', views.CommentViewSet,
                      basename='post-comments')


urlpatterns = router.urls + posts_router.urls
