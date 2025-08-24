from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UserProfile
from drf_spectacular.utils import extend_schema

from django.contrib.auth import get_user_model

from .serializers import (
    UserProfileSerializer,
    UserSerializer,
    UserRegisterSerializer,
    AdminRegisterSerializer,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsAdmin, isSelfOrAdmin, ReadOnly, IsProfileOwnerOrAdmin
from rest_framework.permissions import AllowAny


User = get_user_model()

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsProfileOwnerOrAdmin]

class MeView(generics.RetrieveUpdateAPIView):
      
      """
      Get current user info and edit profile (name/phone/address).
      Email & role are read-only here.
      """
      permission_classes=[IsAuthenticated]
      serializer_class = UserSerializer

      def get_object(self):
          return self.request.user

class UserRegisterView(generics.CreateAPIView):
     serializer_class = UserRegisterSerializer
     permission_classes= [AllowAny]
     authentication_classes = []

class AdminRegistrationView(generics.CreateAPIView):
     serializer_class = AdminRegisterSerializer
     permission_classes = [IsAdmin]

class LoginView(TokenObtainPairView):
    """
    Returns access & refresh JWT tokens.
    """
    permission_classes = [AllowAny]


class RefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

class LogoutView(APIView):
     permission_classes = [IsAuthenticated]
     """Blacklist a refresh token to 'logout' """

     @extend_schema(
               request={
                    'application/json':{
                         'type': 'object',
                         'properties': {
                              'refresh': {'type': 'string'}
                         },
                         'required': ['refresh']
                    }
               },
               responses={
                    205: {'description': 'Successfully logged out'},
                    400: {'description': 'Invalid token'}
               }
               
     )

     def post(self, request):
          try:
               refresh = RefreshToken(request.data["refresh"])
               refresh.blacklist()
               return Response({"detail": "Logged out"}, status=status.HTTP_205_RESET_CONTENT)
          except Exception:
               return Response({"detail": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)