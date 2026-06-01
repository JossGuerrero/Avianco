# vuelos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from vuelos.views.health     import health_check
from vuelos.views.auth       import RegisterView, LogoutView
from vuelos.views.user       import UserViewSet
from vuelos.views.aeropuerto import AeropuertoViewSet
from vuelos.views.aeronave   import AeronaveViewSet
from vuelos.views.vuelo      import VueloViewSet
from vuelos.views.pasajero   import PasajeroViewSet
from vuelos.views.reserva    import ReservaViewSet
from vuelos.serializers.auth import CustomTokenView

router = DefaultRouter()
router.register('usuarios',    UserViewSet,       basename='usuario')
router.register('aeropuertos', AeropuertoViewSet, basename='aeropuerto')
router.register('aeronaves',   AeronaveViewSet,   basename='aeronave')
router.register('vuelos',      VueloViewSet,      basename='vuelo')
router.register('pasajeros',   PasajeroViewSet,   basename='pasajero')
router.register('reservas',    ReservaViewSet,    basename='reserva')

urlpatterns = [
    path('health/',             health_check),
    path('auth/registro/',      RegisterView.as_view()),
    path('auth/login/',         CustomTokenView.as_view()),
    path('auth/token/refresh/', TokenRefreshView.as_view()),
    path('auth/token/verify/',  TokenVerifyView.as_view()),
    path('auth/logout/',        LogoutView.as_view()),
    path('', include(router.urls)),
]