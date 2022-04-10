from django.contrib import admin
from .models import *

# Register your models here.
class TipoTransaccionAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('nombre_tipo',)
    ordering = ('nombre_tipo',)
    search_fields = ('nombre_tipo',)

    class Meta:
        model = TipoTransaccion

class TransaccionAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'modify_at')
    list_display = ('transaccion','usuario','concepto', 'valor_recaudo','modify_at')
    ordering = ('transaccion',)
    search_fields = ('transaccion','usuario','concepto', 'valor_recaudo','modify_at')

    class Meta:
        model = Transaccion

admin.site.register(TipoTransaccion, TipoTransaccionAdmin)
admin.site.register(Transaccion, TransaccionAdmin)

