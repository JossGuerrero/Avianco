from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from vuelos.models import Factura
from vuelos.serializers.factura import FacturaSerializer
from vuelos.pagination import StandardPagination
from rest_framework.permissions import IsAuthenticated


class FacturaViewSet(viewsets.ModelViewSet):
    queryset           = Factura.objects.select_related('reserva').all()
    serializer_class   = FacturaSerializer
    permission_classes = [IsAuthenticated]
    pagination_class   = StandardPagination
    filter_backends    = [DjangoFilterBackend, OrderingFilter]
    filterset_fields   = ['estado', 'reserva']
    ordering_fields    = ['-fecha']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(reserva__pasajero__usuario=self.request.user)
