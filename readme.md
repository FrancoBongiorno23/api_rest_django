# Pruebas automatizadas de API REST Bongiorno Nestor Antonio

## Primero indicamos cual es el ejemplo de la API en la cual se realizara la consigna del testing automatizado, la cual es la API construida en Programación Distribuida I.

* En primer lugar debemos instalar las librerias de python necesarias segun el srchivo requirements.txt 


* Pasos basicos para correr la API

1- Primero corroborar que version de Python poseemos mediante el CMD o "Simbolo de sistema" en caso de ser Windows.

2- Dentro del CMD ingresar los siguientes caracteres para corroborar:
	python --version

3- Corroborar que dicha version es la ultima en el siguiente enlace:
	https://www.python.org/downloads/

4- En caso de ser la ultima version, instalar desde el link del paso 3.

5- Instalar Django desde la consola (CMD), con los siguientes caracteres:
	$ pip install django
(en caso de ya poseerlo instalado solo nos informara que ya existe en el sistema)

6- Una vez dentro de la carpeta de nombre mysite (en el CMD) del archivo enviado, mediante el uso de el comando cd para avanzar o .. en caso de necesitar retroceder, ingresar el siguiente texto:
	python manage.py runserver

7- La API ya esta corriendo y solo se debe de copiar el enlace que le dice la respuesta dem CMD y pegarlo en un navegador para acceder al la misma.



* Pasos para realizar el testing automatizado tomando en cuenta nuestro ejemplo:

1- Ingresar a la carpeta en donde se encuenta nuestra API, en nuestro caso es la ruta: Bongiorno_API_REST\mysite\myapi

2- Luego dirigirse a la seccion de tests, es decir el archivo tests.py, se adjunto la ruta del ejemplo: Bongiorno_API_REST\mysite\myapi\tests.py

3- Dentro del archivo tests.py borrar la clase de test de django Testcase, por ende la borramos, debido a que Django nos provee un testcase para API especifico.

4- Importamos las librerias que utilizaremos en este test, las cuales se escribe el codigo a continuacion:
	
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
	
	
	



	
	

