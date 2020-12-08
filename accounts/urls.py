from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.logar, name='login'),
    path('register/', views.register, name='register'),
]
