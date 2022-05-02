from rest_framework import serializers

from .models import Libro, Lector

class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ('editorial_nombre', 'id','isbn', 'titulo', 'fechaLanzamiento', 'idioma', 'paginas', 'descripcion', 'peso')

        
    editorial_nombre = serializers.SerializerMethodField('get_editorial_nombre')

    def get_editorial_nombre(self, obj):
        return obj.editorial.nombre

#elimine las foreign keys lo cual da error de POST pero muestra el GET


class LectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lector
        fields = ('id','nombre', 'apellido', 'correo')
