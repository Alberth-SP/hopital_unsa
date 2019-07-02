from django.db import models
from apps.Administrador.models import Area, Personal, TipoUsuario, Usuario
from apps.Admision.models import HorarioCab, HorarioDet, Paciente, Provincia, Distrito, Departamento, GrupSang, HistoriaCab

#from apps.Consultorio.models import Triaje, Cita, Consulta, Especialidad, Especialista, 
# HistoriaDet

class Especialidad(models.Model):
    codigoEsp = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200,blank=True,null=True)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class Especialista(models.Model):
    #FK Codigo Persona
    personal= models.OneToOneField(Personal, on_delete=models.CASCADE, primary_key=True)
    #FK Codigo Especialidad
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE,null=True)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.personal.__str__() + " - "+ self.especialidad.__str__()

class Triaje(models.Model):
    codigoTriaje = models.AutoField(primary_key=True)
    #FK Personal
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE,null=True)
    #FK Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True)
    talla = models.FloatField()
    peso = models.FloatField()
    temperatura = models.FloatField()
    frecuenciaR = models.IntegerField()
    frecuenciaC = models.IntegerField()
    presionArt = models.IntegerField()
    fechaReg = models.DateTimeField(auto_now=True)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return str(self.codigoTriaje)



class Cita(models.Model):
    codigoCita = models.AutoField(primary_key=True)
    #FK Especialidad
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE,null=True)
    #FK Especialista
    especialista = models.ForeignKey(Especialista, on_delete=models.CASCADE,null=True)
    #FK Nro historia
    historia = models.ForeignKey(HistoriaCab, on_delete=models.CASCADE,null=True)
    numeroRecibo = models.IntegerField(unique=True)
    fechaSeparacion = models.DateTimeField(blank=True,null=True)
    fechaAtencion = models.DateTimeField(blank=True,null=True)
    #######Especificar tipos estado turno condicion
    estadoCita = models.CharField(max_length=10,blank=True,null=True)
    turno = models.CharField(max_length=10,blank=True,null=True)
    condicion = models.CharField(max_length=10,blank=True,null=True)
    estReg = models.CharField(max_length=1)


    def __str__(self):
        return str(self.codigoCita)

class Consulta(models.Model):
    codigoConsulta = models.AutoField(primary_key=True)
    #FK Cita
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE,null=True)
    #FK Triaje
    triaje = models.ForeignKey(Triaje, on_delete=models.CASCADE,blank=True,null=True)
    horaEntrada = models.DateTimeField(blank=True,null=True)       
    horaSalida = models.DateTimeField(blank=True,null=True)  
    motivoConsulta = models.TextField(blank=True,null=True)
    apetito = models.CharField(max_length=100,blank=True,null=True)
    orina = models.CharField(max_length=100,blank=True,null=True)
    deposiciones = models.CharField(max_length=100,blank=True,null=True)
    examenFisico = models.CharField(max_length=100,blank=True,null=True)
    diagnostico = models.TextField(blank=True,null=True)
    tratamiento = models.TextField(blank=True,null=True)
    proximaCita = models.DateTimeField(blank=True,null=True)
    estReg = models.CharField(max_length=1)
    estadoAtencion = models.CharField(max_length=1,blank=True,null=True)
    motivoAnulacion = models.TextField(blank=True,null=True)

    def __str__(self):
        return str(self.codigoConsulta)
   
class  HistoriaDet(models.Model):
    #PFK NumeroHistoria
    numeroHistoria = models.ForeignKey(HistoriaCab, on_delete=models.CASCADE)
    #FK Consulta
    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)

    def __str__(self):
        return self.numeroHistoria.__str__()
   