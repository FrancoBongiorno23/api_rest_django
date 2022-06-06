import json
import unittest

# from django.contrib.auth.models import User
from django.urls import reverse
# esta era la anterior linea from profiles.api.serializers import ProfileSerializer
# esta linea deberia ir  from rest_framework import ProfileSerializer
# dejo este en comentario from rest_framework import Profile
from rest_framework import status

# from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class RegistrationTestCase(APITestCase):

    def setUp(self):
        self.data = ("nombre", "apellido", "correo")

    def test_correct_registration(self):
        data = {"nombre": "ejemplo", "apellido": "ejemploapellido" ,
                "correo": "correo@testing.com"}
        response=self.client.post("/lectores/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_blank_registration(self):
        data = {"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.post("/lectores/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST); 
        self.assertEqual(3, len(response.data))
        self.assertEqual("This field may not be blank.", response.data["nombre"][0])

    def test_method_not_allowed(self):
        data = {"id":"100" ,"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.post("/lectores/100/", data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_notfound(self):
        data = {"id":"100" ,"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.get("/lectores/100/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch(self):
        data = {"nombre": "Max", "apellido": "Power" ,
                "correo": "mevoy@actualizar.net"}
        response=self.client.patch("/lectores/9/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        
  

#el error actualmente radica en que el metodo setUp importado de unittest no esta definido correctamente porque no poseo la variable con la cual quiero crear el metodo
