from django.db import models
from django.db.models.fields import CharField, DateField, FloatField, IntegerField
from django.db.models.fields.related import ForeignKey
from CitasVentas.models import OrdenCompra

class Material (models.Model):
    tipoMaterial = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    tipoUnidad = models.CharField(max_length=200)

    def __str__(self):
        return self.tipoMaterial

class ProductoTerminado (models.Model):
    id = models.IntegerField(primary_key=True)
    id_ordenCompra = models.ForeignKey(OrdenCompra, on_delete=models.SET_NULL, null=True)
    fecha = models.DateField()
    tipoJoya = models.CharField(max_length=200)
    tipoMaterial = models.ForeignKey(Material, on_delete=models.CASCADE)
    manoObra = models.FloatField(default=0)
    talla = models.CharField(max_length=200)
    ancho = models.FloatField(default=0)
    engaste = models.FloatField(default=0)
    render = models.FloatField(default=0)

    def __str__(self):
        return self.tipoJoya
    




class CuentaCobro (models.Model):
    fecha = models.DateField()
    id_1 = models.ForeignKey(ProductoTerminado, on_delete=models.CASCADE)
    precio = models.ForeignKey(Material, on_delete=models.CASCADE)
    oro = models.FloatField(default=0)
    piedraPreciosa = models.FloatField(default=0)
    manoObra = models.FloatField(default=0)
    render = models.FloatField(default=0)

    def __str__(self): 
        return self.precio
    

