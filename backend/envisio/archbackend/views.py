from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import users

class UserView(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = UserSerializer