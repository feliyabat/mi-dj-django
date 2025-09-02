from django.contrib import admin
from .models import Cliente, Empleado, Orden, DetalleOrden, Producto, Proveedor, Categoria

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'cli_nombre', 'cli_ciudad', 'cli_pais', 'cli_telefono', 'cli_mail')
    search_fields = ('id_cliente', 'cli_nombre', 'cli_contacto', 'cli_ciudad', 'cli_pais', 'cli_mail')
    list_filter = ('cli_pais', 'cli_region')


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'emp_nombre', 'emp_apellido', 'emp_titulo', 'emp_mail', 'emp_fecha_contrato')
    search_fields = ('emp_nombre', 'emp_apellido', 'emp_mail')
    list_filter = ('emp_titulo', 'emp_fecha_contrato')


class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 0
    autocomplete_fields = ('producto',)


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'id_cliente', 'id_empleado', 'ord_fecha')
    list_filter = ('ord_fecha', 'id_empleado')
    search_fields = ('id_cliente__cli_nombre', 'id_empleado__emp_nombre', 'id_empleado__emp_apellido', 'id_orden')
    date_hierarchy = 'ord_fecha'
    inlines = [DetalleOrdenInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'pro_nombre', 'id_categoria', 'id_proveedor', 'pro_precio', 'pro_stock')
    search_fields = ('pro_nombre', 'pro_descripcion', 'id_categoria__cat_nombre', 'id_proveedor__prv_empresa')
    list_filter = ('id_categoria', 'id_proveedor')
    autocomplete_fields = ('id_categoria', 'id_proveedor')


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'prv_empresa', 'prv_giro', 'prv_telefono')
    search_fields = ('prv_empresa', 'prv_giro', 'prv_contacto')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'cat_nombre')
    search_fields = ('cat_nombre', 'cat_desc')