from django.db import models
from apps.Admision.models import HorarioCab, HorarioDet, Paciente, Provincia, Distrito, Departamento, GrupSang, HistoriaCab

class TipoExamen(models.Model):
    codigoTExam= models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estReg = models.CharField(max_length=1)

class ExamenLabCab(models.Model):
    codigoExam= models.IntegerField(primary_key=True)
    #FK Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    #FK TipoExam
    tipoExam = models.ForeignKey(TipoExamen, on_delete=models.CASCADE)
    orden = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    muestra = models.CharField(max_length=100)
    resultado = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=200)

class  ExamenLabDet(models.Model):
    #PFK ExamLabCab
    codigoExam = models.ForeignKey(ExamenLabCab, on_delete=models.CASCADE, primary_key=True)
    descripcion = models.CharField(max_length=100)
    resultadoObtenido = models.DateTimeField()
    situacion = models.CharField(max_length=100)
    rangoReferencia = models.CharField(max_length=100)
   