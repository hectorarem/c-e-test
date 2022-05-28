from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client

c = Client()

class AuthTestCase(TestCase):
    api = '/api/v1/auth/'
    def setUp(self):
        User.objects.create_user(username="man", email='man@gmail.com', password='zaqwsxcde123/*-+')

    def test_login(self):
        """users can login"""
        response = c.post(f'{self.api}login', {"username": "man", "password": "zaqwsxcde123/*-+"})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = c.post(f'{self.api}login', {"username": "man", "password": "zaqwsxcde123/*-+"})
        self.assertEqual(response.status_code, 200)
        if response.status_code == 200:
            access = response.json()['access']
            refresh_token = response.json()['refresh']
            logout = c.post(f'{self.api}logout/', data={'refresh_token': refresh_token}, HTTP_AUTHORIZATION=f"Bearer {access}")
            self.assertEqual(logout.status_code, 205)

    def test_register(self):
        data = {
            "username": 'man2',
            "password": 'zaqwsxcde123/*-+2',
            'email': 'man2@gmail.com',
        }
        response = c.post(f'{self.api}register/', data=data)
        self.assertEqual(response.status_code, 201)
