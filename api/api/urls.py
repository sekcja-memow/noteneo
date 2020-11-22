from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from api.example import views

router = routers.DefaultRouter()
router.register(r'hello', views.HelloViewSet, basename='hello')
router.register(r'hello_auth', views.AuthHelloViewSet, basename='hello_auth')

urlpatterns = [
    path('', include(router.urls)),
    path('auth', auth_views.obtain_auth_token)
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
