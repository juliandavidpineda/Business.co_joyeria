from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from Fabrica.serializers import *

class MaterialAPI (viewsets.ModelViewSet):
    serializer_class = MaterialSerial
    queryset = Material.objects.all()


class ProductoTerminadoAPI (viewsets.ModelViewSet):
    serializer_class = ProductoTerminadoSerial
    queryset = ProductoTerminado.objects.all()

class CuentaCobroAPI (viewsets.ModelViewSet):
    serializer_class = CuentaCobroSerial
    queryset = CuentaCobro.objects.all()
    

