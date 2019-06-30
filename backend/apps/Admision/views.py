from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status

from apps.Consultorio.models import Cita
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from apps.Admision.serializers import CitasSerializer


#def reservarCitas(request):
 #       serializer = CitasSerializer(data=request.data)
  #      if serializer.is_valid():
   #         serializer.save()
    #        print(3)
     #       return Response(serializer.data, status=status.HTTP_201_CREATED)
      #  print(4)
       # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.views import APIView


class listaCitas(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitasSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset,
            pk=self.kwargs['pk']
        )
    def post(self, request, format=None):
        serializer = CitasSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            print("2")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class reservarCita(generics.ListCreateAPIView):
    queryset = Cita.objects.all()
    serializer_class = CitasSerializer


    def post(self, request, format=None):
        serializer = CitasSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            print("2")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def listarCitas(request):
    c = Cita.objects.all()
    print(c)
    return HttpResponse(c)