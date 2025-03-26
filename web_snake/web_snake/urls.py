"""URL configuration for web_snake project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # path('', include('rating.urls')),
    path('admin/', admin.site.urls),
    # path('auth/', include('django.contrib.auth.urls')),
    # path('api/', include('api.urls')),
    path('pages/', include('pages.urls')),
]

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
