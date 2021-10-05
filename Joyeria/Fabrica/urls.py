from django.urls import path, include
from rest_framework import routers, urlpatterns

from rest_framework.routers import DefaultRouter
from Fabrica.serializers import ProductoTerminadoSerial

from Fabrica.views import CuentaCobroAPI, MaterialAPI, ProductoTerminadoAPI

router = DefaultRouter()
router.register('material', MaterialAPI)
router.register('productoTerminado', ProductoTerminadoAPI)
router.register('cuentaCobro', CuentaCobroAPI)

urlpatterns =[
    path('crud/',include(router.urls))
]