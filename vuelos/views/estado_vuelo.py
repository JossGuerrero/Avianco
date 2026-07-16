from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import EstadoVuelo
from vuelos.serializers import EstadoVueloSerializer
from vuelos.pagination import StandardPagination
from vuelos.permissions import LecturaPublicaEscrituraStaff

class EstadoVueloViewSet(viewsets.ModelViewSet):
    queryset           = EstadoVuelo.objects.select_related('vuelo').all()
    serializer_class   = EstadoVueloSerializer
    permission_classes = [LecturaPublicaEscrituraStaff]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['vuelo', 'estado']
    ordering_fields    = ['-fecha']
