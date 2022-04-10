from pyexpat import model
from django.contrib import admin
from .models import *

# Register your models here.
class EmpleadosAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at','estado')  # no permite modificar estos campos
    list_display = ('usuario', 'cargo', 'contrato','estado')
    ordering = ('cargo','contrato')
    search_fields = ('cargo',)

    class Meta:
        model = Empleados

class IngresoEmpleadoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')  # no permite modificar estos campos
    list_display = ('empleado', 'periodo', 'ingreso_bruto','create_at')
    ordering = ('empleado','periodo')
    search_fields = ('empleado',)

class DatosEmpleadosAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('usuario', 'ingresos_empleado', 'total_egresos','monto_maximo_cuota', 'persona_contacto','telefonos_contacto')
    ordering = ('usuario',)
    search_fields = ('usuario','ingresos_empleado', 'total_egresos', 'persona_contacto','telefonos_contacto','tipo_vivienda')

    class Meta:
        model = DatosEmpleado

    # Función para traer elementos de otra tabla deacuerdo a la llave foranea
    def ingresos_empleado(self, obj):
        return obj.ingresos.ingreso_bruto
    
    
    def monto_maximo_cuota(self, obj):
        """ 
        Función para obtener el máximo de prestamo, se determina que solo 
        se puede prestar el 80% del resultado de restar los egresos de los ingresos
        """
        ingreso = obj.ingresos.ingreso_bruto
        egreso = obj.total_egresos
        prestamo = ((ingreso - egreso)/100) * 80
        return prestamo


admin.site.register(Empleados, EmpleadosAdmin)
admin.site.register(IngresosEmpleado, IngresoEmpleadoAdmin)
admin.site.register(DatosEmpleado, DatosEmpleadosAdmin)

