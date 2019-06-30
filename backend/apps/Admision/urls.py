
from .views import *
from django.urls import path
urlpatterns = [
    path('grupsang/', GrupSangList.as_view(), name='grupsang'),
    path('distrito/', DistritoList.as_view(), name='distrito'),
    path('provincia/', ProvinciaList.as_view(), name='provincia'),
    path('departamento/', DepartamentoList.as_view(), name='departamento')
]