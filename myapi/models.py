from django.db import models
#Pongo nombres de modelos en singular ej. LIbro

class Autor(models.Model):
    #id=models.AutoField(primary_key = True)
    apellido=models.CharField(max_length = 120)
    nombre=models.CharField(max_length = 100)
    email=models.EmailField(max_length=200)

    def __str__(self):
        return self.apellido


class Editorial(models.Model):
    id=models.AutoField(primary_key = True)
    nombre=models.CharField(max_length = 120)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    id=models.AutoField(primary_key = True)
    nombre=models.CharField(max_length = 120)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    id=models.AutoField(primary_key = True)
    isbn=models.CharField(max_length=20)
    titulo=models.CharField(max_length = 100)
    fechaLanzamiento=models.DateField()
    #idAutor= models.ForeignKey(Autor, on_delete=models.CASCADE)
    idCategoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    idEditorial= models.ForeignKey(Editorial, on_delete=models.CASCADE)
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


class Alquiler(models.Model):
    id=models.AutoField(primary_key = True)
    idLector=models.ForeignKey(Lector, on_delete=models.CASCADE)
    idLibro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    fechaSalida=models.DateField()
    fechaentrada=models.DateField()