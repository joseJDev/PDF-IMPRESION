from unicodedata import name
from django.urls import path

# Vistas
from .views import ListSolicitudes, GeneratePagarePDF, GenerateAutorizacionPDF
urlpatterns = [
    path('', ListSolicitudes.as_view(), name='listar-solicitudes'),
    path('pdf-pagare/<int:pk>/', GeneratePagarePDF.as_view(), name='pdf-pagare'),
    path('pdf-autorizacion-descuento/<int:pk>/', GenerateAutorizacionPDF.as_view(), name='pdf-autorizacion-descuento'),
]
