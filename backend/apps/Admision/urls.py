
from .views import *
from django.urls import path
urlpatterns = [
    path('grupsang/', GrupSangList.as_view(), name='grupsang')
   # url(r'^historias\$', HistoriasList.as_view(), name='historias')
]