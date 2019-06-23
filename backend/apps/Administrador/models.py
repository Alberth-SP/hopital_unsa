from django.db import models

# Create your models here.

class Area(models.Model):

    codigoArea = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre


class Personal(models.Model):
    codigoPer = models.AutoField(primary_key=True)
    #FK Area
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    dni = models.IntegerField(unique=True)
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    celular = models.CharField(max_length=10,null=False,blank=True)
    telefono = models.CharField(max_length=9,null=False,blank=True)
    direccion = models.CharField(max_length=90,null=False,blank=True)
    email = models.EmailField(null=False,blank=True,unique=False)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombres + " "+self.apellido_paterno+" "+self.apellido_materno
 
class TipoUsuario(models.Model):
    codigoTU = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    #PFK codigoPersonal
    personal= models.OneToOneField(Personal, on_delete=models.CASCADE,primary_key=True)
    #FK codigo TipoUsuario
    tipoUser = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    nombreUser = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30)
    fecha_registro = models.DateField(auto_now=True)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombreUser