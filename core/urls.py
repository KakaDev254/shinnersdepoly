from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('emcee/', views.emcee, name='emcee'),   
    path('gallery/', views.gallery_page, name='gallery'), 
    path('donate/', views.donate_view, name="donate"), 
]