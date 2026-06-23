from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Ciudad
from vuelos.serializers import CiudadSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import EsStaffOSoloLectura

class CiudadViewSet(viewsets.ModelViewSet):
    queryset           = Ciudad.objects.select_related('pais').all()
    serializer_class   = CiudadSerializer
    permission_classes = [EsStaffOSoloLectura]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields   = ['pais']
    search_fields      = ['nombre', 'pais__nombre']
    ordering_fields    = ['nombre']
