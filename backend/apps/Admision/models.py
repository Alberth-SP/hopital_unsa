from django.db import models
from apps.Administrador.models import Area, Personal, TipoUsuario, Usuario


class HorarioCab(models.Model):
    codigoHor = models.IntegerField(primary_key=True)
    dia = models.IntegerField()
    turno = models.IntegerField()
    fechaIicio = models.DateTimeField(auto_now=True)
    fechaFin = models.DateTimeField()
    estReg = models.CharField(max_length=1)

class HorarioDet(models.Model):
    #FK HORARIO
    codigoHor = models.OneToOneField(HorarioCab, on_delete=models.CASCADE)
    #FK PERSONAL
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    dia = models.IntegerField()
    fechaIicio = models.DateTimeField(auto_now=True)
    fechaFin = models.DateTimeField()
    estReg = models.CharField(max_length=1)

class Departamento(models.Model):
    codigoDep = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)   
    estReg = models.CharField(max_length=1)

class Provincia(models.Model):
    codigoPro = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)   
    estReg = models.CharField(max_length=1)

class Distrito(models.Model):
    codigoDist = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)   
    estReg = models.CharField(max_length=1)

class GrupSang(models.Model):
    codigoGS = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=30)   
    estReg = models.CharField(max_length=1)

class Paciente(models.Model):
    codigoPac = models.IntegerField(primary_key=True)
    #FK GrupoSan
    grupoSanguineo = models.ForeignKey(GrupSang, on_delete=models.CASCADE)
    #FK Distrito
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE)
    #FK Provincia
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    #FK Departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    dni = models.IntegerField()
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1)
    fechaNac = models.DateTimeField()
    foto = models.BinaryField()
    celular = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)
    estadoCivil = models.CharField(max_length=15)
    gradoInstruccion = models.CharField(max_length=15)
    ocupacion = models.CharField(max_length=30)
    fechaReg = models.DateTimeField(auto_now=True)
    direccion = models.CharField(max_length=90)
    nacionalidad = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    estReg = models.CharField(max_length=1)

class HistoriaCab(models.Model):
    numeroHistoria = models.IntegerField(primary_key=True)
    #FK PACIENTE
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)