from .models import *
from rest_framework import serializers

class GrupSangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrupSang
        fields = ('codigoGS', 'descripcion', 'estReg')

class DistritoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distrito
        fields = ('codigoDist', 'nombre', 'estReg')

class ProvinciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provincia
        fields = ('codigoPro', 'nombre', 'estReg')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('codigoDep', 'nombre', 'estReg')

class PacienteSerializer(serializers.HyperlinkedModelSerializer):

    grupoSanguineo = GrupSangSerializer(many=True, read_only=True)
    distrito = DistritoSerializer(many=True, read_only=True)
    provincia = ProvinciaSerializer(many=True, read_only=True)
    departamento = DepartamentoSerializer(many=True, read_only=True)

    class Meta:
        model = Paciente
        fields = ('codigoPac','grupoSanguineo', 'distrito', 'provincia', 'departamento', 'dni', 'nombres', 'apellido_paterno', 'apellido_materno', 'sexo', 'fechaNac', 'foto', 'celular', 'telefono', 'estadoCivil', 'gradoInstruccion', 'ocupacion', 'fechaReg', 'direccion','nacionalidad', 'descripcion', 'email', 'estReg')
