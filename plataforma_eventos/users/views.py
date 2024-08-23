from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .permissions import IsOrganizer, IsProvider

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# Vista para Organizador
class OrganizerOnlyView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsOrganizer]

# Vista para Proveedor
class ProviderOnlyView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProvider]

# Vista personalizada para login
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Primero autentica al usuario y luego invalida los tokens antiguos
        response = super().post(request, *args, **kwargs)
        # Invalida tokens anteriores después del login
        if response.status_code == 200:
            user = CustomUser.objects.get(username=request.data['username'])
            RefreshToken.for_user(user)
        return response
