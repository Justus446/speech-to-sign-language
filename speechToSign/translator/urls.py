from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('translate/', views.translate, name='translate'),
    path('quit/', views.quit_app, name='quit'),
]
