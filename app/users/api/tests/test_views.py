import json
from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestViews(APITestCase):

    def test_user_cannot_register_without_credentials(self):
        res = self.client.post(reverse('rest_register'))
        self.assertEqual(res.status_code, 400)

    def test_user_can_register(self):
        user_data = {
            "email":"email@example.com",
            "password1":"P@55w0rd",
            "password2":"P@55w0rd"
        }
        res = self.client.post(reverse('rest_register'), 
            user_data, format="json")
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.json()["detail"], "Verification e-mail sent.")


    def test_user_not_permitted_without_verification(self):
        register_data = {
            "email":"email@example.com",
            "password1":"P@55w0rd",
            "password2":"P@55w0rd"
        }
        login_data = {
            "email":"email@example.com",
            "password":"P@55w0rd"
        }
        reg_res = self.client.post('api/auth/dj-rest-auth/registration/',
            register_data, format='json')
        res = self.client.post('api/auth/dj-rest-auth/login/', 
            login_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_user_can_be_sent_email(self, request):
    #     self.assertEqual(len(mail.outbox), 1)
    #     email_lines = mail.outbox[0].body.splitlines()
    #     activation_line = [l for l in email_lines if "verify-email" in l][0]
    #     activation_link = activation_line.split("go to ")[1]
    #     activation_key = activation_link.split("/")[4]