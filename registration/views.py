# Cargar librerias necesarias para la admin de profile:
from django.shortcuts import render

from .forms import ProfileForm                              # Clases de formularios en forms.py
from django.views.generic.edit import UpdateView            # Vista en clase para actualización de datos
# Decoradores user login in:
from django.utils.decorators import method_decorator        # Método decorador para usuario logueado y uso de la vista:
from django.contrib.auth.decorators import login_required   # Decorador para login requerido
# Cargamos el Modelo de datos:
from .models import Profile
# Cargamos el formulario de creacion de usuarios:
from django.contrib.auth.forms import UserCreationForm      # Formulario por defecto de creación de usuario
from django.urls import reverse_lazy                        # Función para redireccionar a una url
from django import forms                                    # Importamos las propiedades del formulario

# Create your views here.

# Creación de la vista para profile:
@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_form.html'

    # Mostrar el perfil a editar (logueado):
    def get_object(self):
        profile, created = Profile.objects.get_or_create(usuario=self.request.user)
        return profile


