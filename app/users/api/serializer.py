from django.db import transaction
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers, exceptions
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from django.conf import settings

from users.models import User

class UserRegistrationSerializer(RegisterSerializer):
    username = None
    first_name = None
    last_name = None

    def get_cleaned_data(self):
        return {
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        setup_user_email(request, user, [])
        user.save()
        return user


class UserLoginSerializer(LoginSerializer):
    username = None

    def authenticate(self, **options):
        return authenticate(self.context["request"], **options)

    def validate(self, attrs):
        email = attrs.get("email")
        # ip_address = get_client_ip(self.context["request"])[0]
        password = attrs.get("password")
        if email and password:
            '''Check if IP address belongs to account with given email address'''
            try:
                if User.objects.get(email=email):
                    user = authenticate(
                    email=email,
                    password=password,
                    )
                if not user:
                    msg = "Invalid credentials.user"
                    raise serializers.ValidationError(msg, code="authorization")      
            except ObjectDoesNotExist:
                msg = "Invalid credentials.exception"
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = "No email provided."
            raise exceptions.ValidationError(msg)
        attrs["user"] = user

        return attrs