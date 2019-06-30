from django.shortcuts import render
from .serializers import GrupSangSerializer
from rest_framework import generics
from .models import *
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