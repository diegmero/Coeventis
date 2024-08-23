from rest_framework import serializers
from .models import CustomUser
import re

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'password', 'confirm_password',
            'role', 'company', 'nif', 'phone', 'provider_type'
        ]

    def validate(self, data):
        # Validar que las contraseñas coincidan
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Las contraseñas no coinciden")

        # Validar formato del número de teléfono
        phone = data.get('phone')
        if phone and not re.match(r'^\+?1?\d{9,15}$', phone):
            raise serializers.ValidationError(
                "El número de teléfono debe tener entre 9 y 15 dígitos y puede comenzar con '+'."
            )

        # Validación del rol y otros campos específicos
        if data.get('role') == CustomUser.ORGANIZER:
            if data.get('provider_type'):
                raise serializers.ValidationError("Un organizador no puede seleccionar el tipo de proveedor.")
            if not data.get('company') or not data.get('nif'):
                raise serializers.ValidationError("Los organizadores deben proporcionar empresa y NIF.")
        
        if data.get('role') == CustomUser.PROVIDER:
            if not data.get('provider_type'):
                raise serializers.ValidationError("Los proveedores deben seleccionar un tipo de proveedor.")
            if not data.get('company') or not data.get('nif'):
                raise serializers.ValidationError("Los proveedores deben proporcionar empresa y NIF.")

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Si el usuario es organizador, remover 'provider_type'
        if instance.role == CustomUser.ORGANIZER:
            representation.pop('provider_type', None)

        return representation


# CLASE PARA EL USER PROFILE SERIALIZER
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'role', 'company', 'nif', 'phone', 'provider_type'
        ]

    def validate(self, data):
        # Validar que el usuario no pueda cambiar de rol una vez creado
        if self.instance.role and data.get('role') != self.instance.role:
            raise serializers.ValidationError("No puedes cambiar tu rol después de registrarte.")
        
        # Validar formato del número de teléfono
        phone = data.get('phone')
        if phone and not re.match(r'^\+?1?\d{9,15}$', phone):
            raise serializers.ValidationError(
                "El número de teléfono debe tener entre 9 y 15 dígitos y puede comenzar con '+'."
            )

        # Validaciones específicas para organizadores y proveedores
        if data.get('role') == CustomUser.ORGANIZER:
            if data.get('provider_type'):
                raise serializers.ValidationError("Un organizador no puede seleccionar el tipo de proveedor.")
            if not data.get('company') or not data.get('nif'):
                raise serializers.ValidationError("Los organizadores deben proporcionar empresa y NIF.")
        
        if data.get('role') == CustomUser.PROVIDER:
            if not data.get('provider_type'):
                raise serializers.ValidationError("Los proveedores deben seleccionar un tipo de proveedor.")
            if not data.get('company') or not data.get('nif'):
                raise serializers.ValidationError("Los proveedores deben proporcionar empresa y NIF.")
        
        return data
