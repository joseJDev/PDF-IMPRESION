from django.contrib import admin
from .models import *

# Register your models here.
class PeriodoAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')   # no permite modificar estos campos
    list_display = ('periodo', )
    ordering = ('periodo', )
    list_filter = ('periodo', )
    search_fields = ('periodo', )

    class Meta:
        model = Periodo 

class MesAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'update_at')   # no permite modificar estos campos
    list_display = ('mes',)
    ordering = ('mes',)
    list_filter = ('mes',)
    search_fields = ('mes',)

    class Meta:
        model = Meses

admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Meses, MesAdmin)