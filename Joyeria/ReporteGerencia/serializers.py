from django.db.models import fields
from rest_framework import serializers

from ReporteGerencia.models import *


class ReporteInformesSerial (serializers.ModelSerializer):
    class Meta:
        model = ReporteInformes
        fields = '__all__'
