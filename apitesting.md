# Pruebas automatizadas de API REST Bongiorno Nestor Antonio

## Primero indicamos cual es el ejemplo de la API en la cual se realizara la consigna del testing automatizado, la cual es la API construida en Programación Distribuida I.

* Pasos para realizar el testing automatizado tomando en cuenta nuestro ejemplo:

1. Ingresar a la carpeta en donde se encuenta nuestra API, en nuestro caso es la ruta: Bongiorno_API_REST\mysite\myapi

2. Luego dirigirse a la seccion de tests, es decir el archivo tests.py, se adjunto la ruta del ejemplo: Bongiorno_API_REST\mysite\myapi\tests.py

3. Dentro del archivo tests.py borrar la clase de test de django Testcase, por ende la borramos, debido a que Django nos provee un testcase para API especifico.

4. Importamos las librerias que utilizaremos en este test, las cuales se escribe el codigo a continuacion:
	
	```python
	import json
	from django.contrib.auth.models import User
	from django.urls import reverse
	from rest_framework.authtoken.models import Token
	from rest_framework.test import APITestCase
	from rest_framework import status
	from profiles.models import Profile
	from profiles.api.serializers import ProfileSerializer
	```

5. Definimos una clase con un nombre que sea sobre lo que intentaremos testear, en este caso como "RegistrationTestCase" debido a que testearemos un log in

6. Definimos los metodos de la clase creada tal que:
	class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "testcase", "email": "correo@testing.com" ,"password1": "passwordstrong-", "password2": "passwordstrong-2"
        }
    response = self.client.post("/api-auth/login/", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	
7. Debemos de adjuntar los datos que introduciremos como usuario nuevo, en este caso son:  "username": "testcase", "email": "correo@testing.com" ,"password1": "passwordstrong-", "password2": "passwordstrong-2" y definimos el endpoint al cual debe de apuntar, en este caso: /api-auth/login/
	
8. Luego para poder correr el mismo y visualizar cual es el error del test, corremos el archivo desde la terminal con:
	python manage.py test
	
9. En mi caso de momento no podre correr el servidor debido a que poseo un error dentro del archivo tests.py donde un import from me genera error. Se estara actualizando en unos dias
	
	
	

