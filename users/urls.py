from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, PasswordViewSet


router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user_view')
router.register(r'password', PasswordViewSet, basename='change_password_view')

urlpatterns = [path('api/', include(router.urls))]