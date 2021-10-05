from django.db.models import fields
from rest_framework import serializers

from Fabrica.models import *

class MaterialSerial (serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class ProductoTerminadoSerial (serializers.ModelSerializer):
    class Meta:
        model = ProductoTerminado
        fields = '__all__'

class CuentaCobroSerial (serializers.ModelSerializer):
    class Meta:
        model = CuentaCobro
        fields = '__all__'


