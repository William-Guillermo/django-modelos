from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# ModelAdmin oermite hacer cambios en el modelo
class ClientesAdmin(admin.ModelAdmin):
    # se utiliza el metodo list_dispaly y se pasa por parametro los campos d elos modelos a mostrar en el panel de admin
    list_display=('nombre','direccion','email','tfono') 
    # Busqueda de informacion por filtros cuando son muchos campos y se requiere hacer una busqueda
    search_fields=('nombre','email','tfono') 

# Register your models here.
# Para tener disponible desde el panel de administracion la tabla de 
# se agrega en el registro, la clase generada anteriormente ClientesAdmin
admin.site.register(Clientes,ClientesAdmin)  
admin.site.register(Articulos) 
admin.site.register(Pedidos)  



