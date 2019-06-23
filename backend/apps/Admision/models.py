from django.db import models
from apps.Administrador.models import Area, Personal, TipoUsuario, Usuario


class HorarioCab(models.Model):
    codigoHor = models.AutoField(primary_key=True)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE,null=True)
    dias = models.IntegerField(blank=True,null=True)
    turno = models.IntegerField(blank=True,null=True)
    fechaInicio = models.DateTimeField(blank=True,null=True)
    fechaFin = models.DateTimeField(blank=True,null=True)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.personal.__str__()

class HorarioDet(models.Model):
    #FK HORARIO
    codigoHor= models.ForeignKey(HorarioCab, on_delete=models.CASCADE,null=True)
    #FK PERSONAL
    
    dia = models.CharField(max_length=12)
    hora_inicio = models.DateTimeField(null=True)
    hora_fin = models.DateTimeField(null=True)
    estReg = models.CharField(max_length=1)
    def __str__(self):
        return self.codigoHor.__str__()

class Departamento(models.Model):
    codigoDep = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,unique=True)   
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    codigoPro = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,unique=True)   
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class Distrito(models.Model):
    codigoDist = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,unique=True)   
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombre

class GrupSang(models.Model):
    codigoGS = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=30,unique=True)   
    estReg = models.CharField(max_length=1)
    def __str__(self):
        return self.descripcion

class Paciente(models.Model):
    CATEGORIES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    )

    codigoPac = models.AutoField(primary_key=True)
    #FK GrupoSan
    grupoSanguineo = models.ForeignKey(GrupSang, on_delete=models.CASCADE,blank=True,null=True)
    #FK Distrito
    distrito = models.ForeignKey(Distrito, on_delete=models.CASCADE,blank=True,null=True)
    #FK Provincia
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,blank=True,null=True)
    #FK Departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,blank=True,null=True)
    dni = models.IntegerField(unique=True)
    nombres = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1,choices=CATEGORIES)
    edad = models.IntegerField(null=True)
    fechaNac = models.DateTimeField(blank=True,null=True)
    foto = models.BinaryField(blank=True,null=True)
    celular = models.CharField(max_length=10,blank=True,null=True)
    telefono = models.CharField(max_length=9,blank=True,null=True)
    estadoCivil = models.CharField(max_length=15,blank=True,null=True)
    gradoInstruccion = models.CharField(max_length=15,blank=True,null=True)
    ocupacion = models.CharField(max_length=30,blank=True,null=True)
    fechaReg = models.DateTimeField(auto_now=True)
    direccion = models.CharField(max_length=90,blank=True,null=True)
    nacionalidad = models.CharField(max_length=30,blank=True,null=True)
    descripcion = models.CharField(max_length=200,blank=True,null=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    estReg = models.CharField(max_length=1)

    def __str__(self):
        return self.nombres + " "+self.apellido_paterno+" "+self.apellido_materno

class  HistoriaCab(models.Model):
    numeroHistoria = models.IntegerField(primary_key=True)
    #FK PACIENTE
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.numeroHistoria)
   
