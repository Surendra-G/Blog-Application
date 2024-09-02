from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AboutUs/', views.about, name='about'), 
    path('ContactUs/', views.contact, name='contact'), 
    path("contents/", views.contents, name='contents'),
    path("profile/", views.profile, name='profile'),
]
