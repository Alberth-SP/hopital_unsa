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