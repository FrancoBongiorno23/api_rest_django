from django.contrib import admin
from .models import Autor, Editorial, Categoria, Libro, Lector, Alquiler


"""myModels = [.models.Autor, .models.Editorial, .models.Categoria, .models.Libro, .models.Lector, .models.Alquiler]  # iterable list
admin.site.register(myModels)"""
# Register your models here.

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Lector)
admin.site.register(Alquiler)