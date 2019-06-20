from django.db import models

# Create your models here.
class Area(models.Model):
    codigoArea = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estReg = models.CharField(max_length=1)

class Personal(models.Model):
    codigoPer = models.IntegerField(primary_key=True)
    #FK Area
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    dni = models.IntegerField()
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    celular = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=90)
    email = models.EmailField(unique=True)
    estReg = models.CharField(max_length=1)
 
class TipoUsuario(models.Model):
    codigoTU = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    estReg = models.CharField(max_length=1)

class Usuario(models.Model):
    #PFK codigoPersonal
    personal= models.OneToOneField(Personal, on_delete=models.CASCADE,primary_key=True)
    #FK codigo TipoUsuario
    tipoUser = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    nombreUser = models.IntegerField()
    password = models.IntegerField()
    fechaIicio = models.DateTimeField(auto_now=True)
    estReg = models.CharField(max_length=1)