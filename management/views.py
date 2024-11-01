from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from management.serializers import UserSerializer
from django.contrib.auth.models import User


class MyTokenObtainPairView(TokenObtainPairView):  
    permission_classes = (permissions.AllowAny,)


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
