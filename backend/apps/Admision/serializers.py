from apps.Consultorio.models import Cita, Especialidad, Especialista
from rest_framework import serializers
from apps.Administrador.models import Personal, Area


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = ['codigoArea', 'nombre', 'estReg']

class PersonalSerializer(serializers.ModelSerializer):

    area = AreaSerializer(many=True, read_only=True)
    class Meta:
        model = Personal
        fields = ['area', 'dni', 'nombres', 'apellido_paterno','apellido_materno','celular','telefono','direccion','email','estReg']


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ['codigoEsp','nombre','descripcion','estReg']

class EspecialistaSerializer(serializers.ModelSerializer):
    # FK Codigo Persona
    personal = PersonalSerializer(many=True, read_only=True)
    especialidad = EspecialidadSerializer(many=True, read_only=True)


    class Meta:
        model = Especialista
        fields = ['personal','especialidad','estReg']



class CitasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cita
        fields = ['codigoCita','especialidad','especialista','numeroRecibo','fechaSeparacion','fechaAtencion','estadoCita','turno','condicion','estReg']