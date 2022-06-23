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

class TestCasesLectores(APITestCase):

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
        data = {"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.post("/lectores/100/", data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_notfound(self):
        data = {"nombre": "", "apellido": "" ,
                "correo": ""}
        response=self.client.get("/lectores/100/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual("N", response.data["detail"][0]) #el error 404 not found da como respuesta "N" al consultar el detalle del mismo


 #desde aca comienzo en libros
class TestCasesLibros(APITestCase):

    def setUp(self):
        self.data = ("isbn", "titulo", "fechaLanzamiento", "idioma", "paginas", "descripcion", "peso")
    
    def test_libros_get(self):
        data = { }
        response=self.client.get("/libros/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_libros_post_a_corregir(self):
        data = {
                "isbn": "1214334",
                "titulo": "Luna de pluton",
                "fechaLanzamiento": "2010-11-06",
                "idioma": "Ingles",
                "paginas": 23,
                "descripcion": "Luna de plutonnn",
                "peso": 1}
        response=self.client.post("/libros/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
