from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile,  name='profile'),
    path('create/', views.create_profile, name='create_profile'),
    path('update_picture/', views.update_profile_picture, name='update_profile_picture'),
    path('setting/', views.users_setting, name='users_setting'),
]
