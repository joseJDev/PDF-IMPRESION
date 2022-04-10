from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View
from empleados.models import Empleados

# Modelos
from fondo.models import SolicitudCredito, DetalleSolicitudes

# PDF
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .functions import FormatNumber

from registration.models import Profile

# Create your views here.


class ListSolicitudes(ListView):
    template_name = 'fondo/order-fondo.html'
    model = SolicitudCredito


class GeneratePagarePDF(View):
    format_num = FormatNumber()
    def get(self, request, *args, **kwargs):
        solicitud_credito = DetalleSolicitudes.objects.filter(solicitud=kwargs['pk']).first()
        profile = Profile.objects.filter(usuario=request.user).first()
        credit_letras = self.format_num.numero_a_letras(solicitud_credito.valor_aprobado)

        pdf = generate_pdf('pdf/pagare-pdf.html',
                           {'detalle': solicitud_credito, 'profile': profile, 'num_letra': credit_letras})
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=pagare_{}.pdf'.format(
            request.user.first_name,
            request.user.last_name
        )

        return response


class GenerateAutorizacionPDF(View):
    format_num = FormatNumber()
    def get(self, request, *args, **kwargs):
        solicitud_credito = DetalleSolicitudes.objects.filter(solicitud=kwargs['pk']).first()
        profile = Profile.objects.filter(usuario=request.user).first()
        empleado = Empleados.objects.filter(usuario=request.user).first()

        credit_letras = self.format_num.numero_a_letras(solicitud_credito.valor_aprobado)
        cuota_letras = self.format_num.numero_a_letras(solicitud_credito.cuotas_pagare)
        valor_cuota_letras = self.format_num.numero_a_letras(solicitud_credito.valor_cuota)

        context_dict = {
            'detalle': solicitud_credito, 
            'empledo': empleado, 
            'profile': profile,
            'credit_letras': credit_letras,
            'cuota_letras': cuota_letras,
            'valor_cuota_letras': valor_cuota_letras
        }

        pdf = generate_pdf(
            'pdf/autorizacion-descuento-pdf.html', context_dict)
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=autorizacion_descuento_{}.pdf'.format(
            request.user.first_name,
            request.user.last_name
        )

        return response


def generate_pdf(template_name, context={}):
    template = get_template(template_name)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        print(type(result))
        return result.getvalue()
    return None
