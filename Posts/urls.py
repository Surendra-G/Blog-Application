from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('AboutUs/', views.about, name='about'), 
    path('ContactUs/', views.contact, name='contact'), 
]
