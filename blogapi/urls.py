from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

admin.site.site_title = 'Blog Post'
admin.site.site_header = 'Blog Post'
urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('blog/', include('blog.urls')),
    path('core/', include('core.urls')),
    path('shcema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/ui/',
         SpectacularSwaggerView.as_view(url_name='schema')),
    path('__debug__/', include('debug_toolbar.urls')),
]
