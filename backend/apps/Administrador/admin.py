from django.contrib import admin
#Administrador
from apps.Administrador.models import Area, Personal, TipoUsuario, Usuario

admin.site.register(Area)
admin.site.register(Personal)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
