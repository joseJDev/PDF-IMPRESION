from django.urls import path 
from django.urls.resolvers import URLPattern

from .views import ProfileUpdate

urlpatterns = [ 
    path("profile/", ProfileUpdate.as_view(),name= "profile"),
 ]