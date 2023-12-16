from django.urls import path, include
from .views import home
from rest_framework import routers

urlpatterns = [
    path('', home, name="home"),
]