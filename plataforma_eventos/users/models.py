from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ORGANIZER = 'organizer'
    PROVIDER = 'provider'
    
    ROLE_CHOICES = [
        (ORGANIZER, 'Organizador'),
        (PROVIDER, 'Proveedor'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='organizer')
    company = models.CharField(max_length=255, blank=True, null=True)
    nif = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20, default='000000000')
    
    # Campos específicos de proveedores
    PROVIDER_TYPES = [
        ('Alojamiento', 'Alojamiento'),
        ('Venue', 'Venue'),
        ('Restaurante/Catering', 'Restaurante/Catering'),
        ('Actividades', 'Proveedor de Actividades'),
        ('Entretenimiento', 'Proveedor de Entretenimiento'),
        ('Decoración', 'Proveedor de Decoración'),
    ]
    provider_type = models.CharField(max_length=50, choices=PROVIDER_TYPES, blank=True, null=True)

    def __str__(self):
        return self.username
