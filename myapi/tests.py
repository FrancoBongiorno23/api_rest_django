import json

from django.contrib.auth.models import User
from django.urls import reverse
# esta era la anterior linea from profiles.api.serializers import ProfileSerializer
# esta linea deberia ir  from rest_framework import ProfileSerializer
# dejo este en comentario from rest_framework import Profile
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"nombre": "ejemplo", "apellido": "ejemploapellido" ,
                "correo": "correo@testing.com"}
        response=self.client.post("/lectores/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED);

class ProfileViewSetTestCase(APITestCase):
        def fail_test_registration(self):
        data = {"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.post("/libros/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST); 
        
  

#el error del enpoint de registro de user radica en la importacion de ProfileSerializer y Profile

#sigo descifrando como es para lograr ver cual es el resultado que te devuelve, en lugar de comparar el status

#el error radicaba en el endpoint donde me confundi el endpoint de /lectores/ con /libros/