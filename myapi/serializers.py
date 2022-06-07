from rest_framework import serializers

from .models import Libro, Lector

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ('id','isbn', 'titulo', 'fechaLanzamiento', 'idioma', 'paginas', 'descripcion', 'peso')

class LectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lector
        fields = ('id','nombre', 'apellido', 'correo')
