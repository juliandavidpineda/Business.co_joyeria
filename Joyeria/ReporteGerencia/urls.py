from django.urls import path, include
from rest_framework import routers, urlpatterns

from rest_framework.routers import DefaultRouter

from ReporteGerencia.serializers import *
from ReporteGerencia.views import *


router = DefaultRouter()
router.register('reporteInformes', ReporteInformesAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]
