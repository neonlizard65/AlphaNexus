"""
URL configuration for alphanexus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'developers', views.DeveloperViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'media', views.MediaViewSet)
router.register(r'libraries', views.LibraryViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'cdkeys', views.CDKeyViewSet)
router.register(r'checks', views.CheckViewSet)
router.register(r'developerrequests', views.DeveloperRequestViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("web.urls")),
    path("api/", include(router.urls))
]
handler404 = "web.views.page404"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)