import json
import unittest

from django.contrib.auth.models import User
from django.urls import reverse
# esta era la anterior linea from profiles.api.serializers import ProfileSerializer
# esta linea deberia ir  from rest_framework import ProfileSerializer
# dejo este en comentario from rest_framework import Profile
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class RegistrationTestCase(APITestCase):

    def setUp(self):
        self.data = data("nombre", "apellido", "correo")

    def test_registration(self):
        data = {"nombre": "ejemplo", "apellido": "ejemploapellido" ,
                "correo": "correo@testing.com"}
        response=self.client.post("/lectores/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def fail_test_registration(self):
        data = {"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.post("/libros/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST); 

        
#el error actualmente radica en que el metodo setUp importado de unittest no esta definido correctamente porque no poseo la variable con la cual quiero crear el metodo