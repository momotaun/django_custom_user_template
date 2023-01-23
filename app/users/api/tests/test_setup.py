from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('rest_register')
        self.login_url = reverse('rest_login')

        self.user_data = {
            "email": "email@example.com",
            "password": "P@55w0rd",
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()