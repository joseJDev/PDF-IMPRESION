from django.db import models

# Create your models here.
from django.db import models
from django.db.models import CASCADE
from datetime import datetime
from core.types.meses import Meses

# Función para extraer el año actual del servidor
def periodoActual():
    hoy = datetime.year
    return hoy

# Create your models here.
class Periodo(models.Model):
    periodo = models.PositiveIntegerField(verbose_name="Año de ejecución", null=False)
    estado_periodo = models.CharField(verbose_name="Estado de Periodo", max_length=20, default="Activo")
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Año de Ejecución'

    def __str__(self) -> str:
        return f'{self.periodo}' 

class Meses(models.Model):
    mes = models.CharField(verbose_name='Mes', max_length=20, choices=Meses, unique=True)
    create_at = models.DateField(auto_now_add=True, null=True, blank=True)
    update_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Mes de Ejecución'

    def __str__(self) -> str:
        return f'{self.mes}'
