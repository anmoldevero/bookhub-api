from django.urls import path,include
from .views import UserViewSet, PasswordViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register(r'users', UserViewSet, basename='user_view')
router.register(r'password', PasswordViewSet, basename='change_password_view')


urlpatterns = [path('api/', include(router.urls))]