from django.urls import path
from .views import RegisterView, UserProfileView, CustomTokenObtainPairView, OrganizerOnlyView, ProviderOnlyView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # Ruta de registro de usuario
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Ruta de login personalizado con invalidación de tokens anteriores
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Ruta para refrescar el token de acceso
    path('profile/', UserProfileView.as_view(), name='user-profile'),  # Ruta para ver y actualizar el perfil de usuario
    path('organizer/', OrganizerOnlyView.as_view(), name='organizer-only'),  # Ruta para ver el perfil de organizador
    path('provider/', ProviderOnlyView.as_view(), name='provider-only'),  # Ruta para ver el perfil de proveedor
]
