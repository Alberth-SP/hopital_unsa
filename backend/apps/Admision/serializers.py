from .models import *
from rest_framework import serializers

class GrupSangSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GrupSang
        fields = ('codigoGS', 'descripcion', 'estReg')
