import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class UserLoginTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="bookrestaurantno1",
            email='bookrestaurantno1@gmail.com',
            password='No123456789@_'
        )
        self.login_url = reverse('login')

    def test_successful_login(self):
        data = {
            'email': 'bookrestaurantno1@gmail.com',
            'password': 'No123456789@_',
        }
        response = self.client.post(self.login_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_invalid_login(self):
    #     data = {
    #         'email': 'bookrestaurantno1@gmail.com',
    #         'password': 'wrongpassword',
    #     }
    #     response = self.client.post(self.login_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(response.data['error'], 'Invalid email or password')