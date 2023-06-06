from django.urls import path
from .views import createUserProfile, updateUserProfile, updatePassword
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', createUserProfile, name='register'),
    path('update-profile/', updateUserProfile, name='update-profile'),
    path('password/', updatePassword, name='update-password'),
]
