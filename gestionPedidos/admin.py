from django.contrib import admin
from gestionPedidos.models import Clientes, Articulos, Pedidos

# ModelAdmin oermite hacer cambios en el modelo
class ClientesAdmin(admin.ModelAdmin):
    # se utiliza el metodo list_dispaly y se pasa por parametro los campos d elos modelos a mostrar en el panel de admin
    list_display=('nombre','direccion','email','tfono') 
    # Busqueda de informacion por filtros cuando son muchos campos y se requiere hacer una busqueda
    search_fields=('nombre','email','tfono') 

class ArticulosAdmin(admin.ModelAdmin):
    #Filtro por seccion
    list_filter=("seccion",)
    #list_filter: _ListOrTuple[_ListFilterT]

class PedidosAdmin(admin.ModelAdmin):
    list_display=('numero','fecha')
    list_filter=('fecha',)  # menu filtrado de la derecha para buscar por fechas
    date_hierarchy='fecha'  #no lleva parentesis ni coma al final , filtro migas de Pan

# Register your models here.
# Para tener disponible desde el panel de administracion la tabla de 
# se agrega en el registro, la clase generada anteriormente ClientesAdmin
admin.site.register(Clientes,ClientesAdmin)  
admin.site.register(Articulos,ArticulosAdmin) 
admin.site.register(Pedidos,PedidosAdmin)  



