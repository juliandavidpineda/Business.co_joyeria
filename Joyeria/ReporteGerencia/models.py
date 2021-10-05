from django.db import models

# Create your models here.

from CitasVentas.models import *

from Fabrica.models import *


class ReporteInformes (models.Model):

    venta = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    infoChat = models.ForeignKey(AgendamientoCitas, on_delete=models.CASCADE)
    MateriaPrima = models.ForeignKey(Material, on_delete=models.CASCADE)
    porAsistir = models.ForeignKey(AgendamientoCitas, on_delete=models.CASCADE)
    asistido = models.ForeignKey(AgendamientoCitas, on_delete=models.CASCADE)

    def __str__(self):
        return self.venta.numOrden

    def reporteVentas(self):
        canVentas = models.venta.objects.filter(numOrden=all).count()
        return canVentas

    def utilidades(self):
        pass

    def informeChats(self):
        chats = models.infoChat.objects.filter(numOrden=all).count()
        return chats

    def stockMateriaPrima(self):
        Materia = models.MateriaPrima.objects.filter(numOrden=all).count()
        return Materia

    def citasPorAsistir(self):
        porAsis = models.porAsistir.objects.filter(numOrden=all).count()
        return porAsis

    def citasAsistidas(self):
        Asis = models.Asistido.objects.filter(numOrden=all).count()
        return Asis
