from django.db import models
from apps.Administrador.models import Area, Personal, TipoUsuario, Usuario
from apps.Admision.models import HorarioCab, HorarioDet, Paciente, Provincia, Distrito, Departamento, GrupSang, HistoriaCab

#from apps.Consultorio.models import Triaje, Cita, Consulta, Especialidad, Especialista, 
# HistoriaDet

class Especialidad(models.Model):
    codigoEsp = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    estReg = models.CharField(max_length=1)

class Especialista(models.Model):
    #FK Codigo Persona
    personal= models.OneToOneField(Personal, on_delete=models.CASCADE, primary_key=True)
    #FK Codigo Especialidad
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    estReg = models.CharField(max_length=1)

class Triaje(models.Model):
    codigoTriaje = models.IntegerField(primary_key=True)
    #FK Personal
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    #FK Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    talla = models.FloatField()
    peso = models.FloatField()
    temperatura = models.FloatField()
    frecuenciaR = models.IntegerField()
    frecuenciaC = models.IntegerField()
    presionArt = models.IntegerField()
    fechaReg = models.DateTimeField()
    estReg = models.CharField(max_length=1)

class Cita(models.Model):
    codigoCita = models.IntegerField(primary_key=True)
    #FK Especialidad
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    #FK Especialista
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE)
    #FK Nro historia
    historia = models.ForeignKey(HorarioCab, on_delete=models.CASCADE)
    numeroRecibo = models.IntegerField()
    fechaSeparacion = models.DateTimeField()
    fechaAtencion = models.DateTimeField()
    #######Especificar tipos estado turno condicion
    estadoCita = models.CharField(max_length=10)
    turno = models.CharField(max_length=10)
    condicion = models.CharField(max_length=10)
    estReg = models.CharField(max_length=1)

class Consulta(models.Model):
    codigoConsulta = models.IntegerField(primary_key=True)
    #FK Cita
    cita = models.ForeignKey(Cita,blank=True, on_delete=models.CASCADE)
    #FK Triaje
    triaje = models.ForeignKey(Triaje, on_delete=models.CASCADE)
    horaEntrada = models.DateTimeField()       
    horaSalida = models.DateTimeField()  
    motivoConsulta = models.CharField(max_length=100)
    apetito = models.CharField(max_length=100)
    orina = models.CharField(max_length=100)
    deposiciones = models.CharField(max_length=100)
    examenFisico = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=200)
    tratamiento = models.CharField(max_length=300)
    proximaCita = models.DateTimeField()
    estReg = models.CharField(max_length=1)
    estadoAtencion = models.CharField(max_length=1)
    motivoAnulacion = models.CharField(max_length=100)
    motivoAnulacion = models.TextField()
   
class  HistoriaDet(models.Model):
    #PFK NumeroHistoria
    numeroHistoria = models.OneToOneField(HistoriaCab, on_delete=models.CASCADE)
    #FK Consulta
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
   