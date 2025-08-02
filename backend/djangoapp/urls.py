from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_us, name='about_us'),
    path('contact/', views.contact_us, name='contact_us'),
    path('get_cars/', views.get_cars, name='get_cars'),
    path('get_dealers/', views.get_dealers, name='get_dealers'),
]
