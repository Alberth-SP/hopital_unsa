from django.shortcuts import render
from .serializers import GrupSangSerializer, DistritoSerializer, ProvinciaSerializer, DepartamentoSerializer, PacienteSerializer
from rest_framework import generics
from .models import *

from rest_framework import generics, status

from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


# Create your views here.

class GrupSangList(generics.ListCreateAPIView):
    queryset = GrupSang.objects.all()
    serializer_class = GrupSangSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj

class DistritoList(generics.ListCreateAPIView):
    queryset = Distrito.objects.all()
    serializer_class = DistritoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj

class ProvinciaList(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj

class DepartamentoList(generics.ListCreateAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
        return obj

class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )

    def post(self, request, format=None):
        serializer = PacienteSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            print("2")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
