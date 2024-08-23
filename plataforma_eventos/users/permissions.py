'''
IsOrganizer: Este permiso restringe el acceso solo a los usuarios con el rol de organizer.
IsProvider: Este permiso restringe el acceso solo a los usuarios con el rol de provider.
'''

from rest_framework import permissions

class IsOrganizer(permissions.BasePermission):
    """
    Permiso personalizado que solo permite el acceso a organizadores.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'organizer'

class IsProvider(permissions.BasePermission):
    """
    Permiso personalizado que solo permite el acceso a proveedores.
    """
    def has_permission(self, request, view):
        return request.user and request.user.role == 'provider'
