from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Profile, Country
from .serializers import ProfileSerializer, CountrySerializer
from .permissions import UpdateOwner


class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        UpdateOwner
    ]