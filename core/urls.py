from django.urls import path
# Importar las vistas:
from .views import HomePageView, TeamPageView, LineasPageView

urlpatterns = [
   path('', HomePageView.as_view(), name='inicio'),
   path('team/', TeamPageView.as_view(), name='team'),
   path('linea-creditos/', LineasPageView.as_view(), name='linea')

]
