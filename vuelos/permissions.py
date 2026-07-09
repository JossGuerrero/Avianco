from rest_framework.permissions import BasePermission, SAFE_METHODS


class EsStaffOSoloLectura(BasePermission):
    """Staff puede todo, usuarios autenticados solo leer."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user and request.user.is_authenticated
        return request.user and request.user.is_staff


class LecturaPublicaEscrituraStaff(BasePermission):
    """Cualquiera puede leer (sin login), solo staff puede escribir."""

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff