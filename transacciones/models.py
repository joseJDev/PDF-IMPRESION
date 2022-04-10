from django.db import models
from django.contrib.auth.models import User
from fondo.models import SolicitudCredito
from django.db.models import CASCADE

# Create your models here.
class TipoTransaccion(models.Model):
    nombre_tipo = models.CharField(verbose_name='Tipo de Transacción', max_length=20, null=False)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Tipo de Transacción'

    def __str__(self) -> str:
        return f'{self.nombre_tipo}'

class Transaccion(models.Model):
    transaccion = models.ForeignKey(TipoTransaccion, on_delete=CASCADE, verbose_name='Tipo de Transacción')
    usuario = models.ForeignKey(User, on_delete=CASCADE, verbose_name='Usuario')
    concepto = models.ForeignKey(SolicitudCredito, on_delete=CASCADE, verbose_name="Concepto")
    valor_recaudo = models.DecimalField(verbose_name='Valor a Recaudar', max_digits=10, decimal_places=2, null=False)
    create_at = models.DateField(auto_now=False, auto_now_add=True, verbose_name="Fecha de creación", null=True, blank=True) 
    modify_at = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Fecha de actualización", null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Transacciones'

    def __str__(self) -> str:
        return f'{self.transaccion} - {self.concepto}'



