
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CitasVentas/api/', include('CitasVentas.urls')),
    path('Fabrica/api/', include('Fabrica.urls'))
]
