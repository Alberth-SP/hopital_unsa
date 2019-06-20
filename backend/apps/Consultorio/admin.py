from django.contrib import admin
#Consultorio
from apps.Consultorio.models import Triaje, Cita, Consulta, Especialidad, Especialista, HistoriaDet

admin.site.register(Triaje)
admin.site.register(Cita)
admin.site.register(Consulta)
admin.site.register(Especialidad)
admin.site.register(Especialista)
admin.site.register(HistoriaDet)