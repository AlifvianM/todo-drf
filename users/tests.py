from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.urls import reverse

from .models import CustomUser

class AuthenticationTest(APITestCase):

    def test_create_account(self):
        url = reverse('register')
        data = {
            'email':'email@email.com',
            'password' : 'sembarang',
            'password2': 'sembarang'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get().email, 'email@email.com')
    
    def test_login_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('login')
        data = {
            'email':'email@email.com',
            'password' : 'sembarang',
            # 'password2': 'sembarang'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_token(self):
        token = Token.objects.get(user__email='Alifvianm@gmail.com')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)