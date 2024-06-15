"""
URL configuration for CareersBucket project.

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
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from Apps.app.urls import *
from Web.web_app.urls import *
from django.conf.urls.static import static
from django.conf import settings


schema_view = get_schema_view(
    openapi.Info(
        title="Your Career's Path",
        default_version='v1',
        description="CRUD for job updated ",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="admin@careersbucket.com"),
        license=openapi.License(name="Career's Bucket License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Apps.app.urls')),
    path('',include('Web.web_app.urls')),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
