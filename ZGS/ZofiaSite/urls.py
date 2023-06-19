from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('gallery/', views.gallery, name='gallery'),
    
    path('home_en', views.home_en, name="home_en"),
    path('profile_list_en/', views.profile_list_en, name='profile_list_en'),
    path('login_en/', views.login_user_en, name='login_en'),
    path('register_en/', views.register_user_en, name='register_en'),
    path('gallery_en/', views.gallery_en, name='gallery_en'),
]
