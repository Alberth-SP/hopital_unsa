from django.db import models
from apps.Admision.models import HorarioCab, HorarioDet, Paciente, Provincia, Distrito, Departamento, GrupSang, HistoriaCab

class TipoExamen(models.Model):
    codigoTExam= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return str(self.nombre)

class ExamenLabCab(models.Model):
    codigoExam= models.AutoField(primary_key=True)
    #FK Paciente
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,blank=True,null=True)
    #FK TipoExam
    nombre_paciente = models.CharField(max_length=100,null=True)
    tipoExam = models.ForeignKey(TipoExamen, on_delete=models.CASCADE)
    orden = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now=True)
    muestra = models.CharField(max_length=100)
    resultado = models.TextField()
    valor = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True,null=True)

    def __init__(self, *args, **kwargs):
        super(ExamenLabCab, self).__init__(*args, **kwargs)
        if self.paciente:
            self.nombre_paciente = self.paciente.__str__()



    def __str__(self):
        return str(self.codigoExam)
   

class  ExamenLabDet(models.Model):
    #PFK ExamLabCab
    codigoExam = models.OneToOneField(ExamenLabCab, on_delete=models.CASCADE, primary_key=True)
    descripcion = models.CharField(max_length=100,blank=True,null=True)
    resultadoObtenido = models.TextField()
    situacion = models.CharField(max_length=100)
    rangoReferencia = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.codigoConsulta.__str__()
   
   