from django.contrib import admin

#Admision
from apps.Admision.models import HorarioCab, HorarioDet, Paciente, Provincia, Distrito, Departamento, GrupSang, HistoriaCab

admin.site.register(HorarioCab)
admin.site.register(HorarioDet)
admin.site.register(Paciente)
admin.site.register(Provincia)
admin.site.register(Distrito)
admin.site.register(Departamento)
admin.site.register(GrupSang)
admin.site.register(HistoriaCab)
