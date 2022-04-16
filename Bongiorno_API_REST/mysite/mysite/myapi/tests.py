import json

from django.contrib.auth.models import User
from django.urls import reverse
from profiles.api.serializers import ProfileSerializer
from profiles.models import Profile
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testcase", "email": "correo@testing.com" ,
                "password1": "passwordstrong-", "password2": "passwordstrong-2"}
    response = self.client.post("/api-auth/login/", data)
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
