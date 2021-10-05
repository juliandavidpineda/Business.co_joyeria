from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework.serializers import Serializer

from ReporteGerencia.serializers import *

# Create your views here.


class ReporteInformesAPI (viewsets.ModelViewSet):
    serializer_class = ReporteInformesSerial
    queryset = ReporteInformes.objects.all()
