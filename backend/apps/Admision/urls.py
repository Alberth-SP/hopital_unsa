from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Admision.views import listaCitas, reservarCita


urlpatterns = [
    url('listar', listaCitas.as_view(),name = "listacitas"),
    url('reservar', reservarCita.as_view() ,name = "reservacita")
]

urlpatterns = format_suffix_patterns(urlpatterns)