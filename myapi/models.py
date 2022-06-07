from django.db import models
#Pongo nombres de modelos en singular ej. LIbro

class Libro(models.Model):
    id=models.AutoField(primary_key = True)
    isbn=models.CharField(max_length=20)
    titulo=models.CharField(max_length = 100)
    fechaLanzamiento=models.DateField()
    idioma=models.CharField(max_length = 100)
    paginas=models.IntegerField()
    descripcion=models.TextField(max_length = 400)
    peso=models.IntegerField()

    def __str__(self):
        return self.titulo


class Lector(models.Model):
    id=models.AutoField(primary_key = True)
    nombre=models.CharField(max_length = 100)
    apellido=models.CharField(max_length = 120)
    correo=models.EmailField(max_length=200)

    def __str__(self):
        return self.nombre

