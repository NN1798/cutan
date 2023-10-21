from django.urls import path, include
from rest_framework import routers

from .views import ProfileView


urlpatterns = [
    path('<int:pk>/', ProfileView.as_view()),
]
