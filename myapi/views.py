from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import LibroSerializer, LectorSerializer
from .models import Libro, Lector


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()#.order_by('titulo')
    serializer_class = LibroSerializer

class LectorViewSet(viewsets.ModelViewSet):
    queryset = Lector.objects.all().order_by('nombre')
    serializer_class = LectorSerializer
