from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from fondo.models import LineaCredito
from django.db import connection

# Create your views here.
class HomePageView(TemplateView):
    # Atributo que indica que template html debe usar:
    template_name = 'core/index.html'
    cursor = connection.cursor()
    sql = 'SELECT * FROM femel.Notificaciones_Solicitudes';
    cursor.execute(sql)
    tabla = []
    for row in cursor.fetchall():
        tabla.append(row)
    

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'titulo': 'FEMEL',
            'mensaje': 'Prototipo funcional para la administración de fondos de empleados',
            'boton': 'Ingresar',
            'data': self.tabla
        })

class TeamPageView(TemplateView):
    template_name = 'core/team.html'
    team_dict = {
        'autor': 'María Estefany Morales Ramos',
        'universidad': 'Institución Universitaria Politécnico Grancolombiano',
        'facultad': 'Facultad, Departamento (Diseño, Ingeniería e innovación)',
        'ubicacion' : 'Medellín, Colombia',
        'periodo' : '2021',
        'repositorio': 'https://github.com/EstefanyRamos94/Femel'
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.team_dict)

class LineasPageView(ListView):
    template_name = 'core/lineas.html'
    model = LineaCredito

    # def get(self, request, *args, **kwargs):
    #     return render(request, self.template_name, self.datos)