from django.contrib import admin
from gestionPedidos.models import Clientes

# Register your models here.
# Para tener disponible desde el panel de administracion la tabla de Clientes
admin.site.register(Clientes)  
