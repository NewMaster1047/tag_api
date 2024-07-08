"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Tag_service API",

        default_version='v1', ),
    public=True,
    permission_classes=[AllowAny, ],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tag/', include('tag.urls')),



    path('swager/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),


    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})

]
