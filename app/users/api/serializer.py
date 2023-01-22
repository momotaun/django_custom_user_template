from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.conf import settings

from users.models import User

class UserRegistrationSerializer(RegisterSerializer):
    username = None
    first_name = None
    last_name = None
    password1 = serializers.CharField(required=True, write_only=True)
    password2 = serializers.CharField(required=True, write_only=True)
    
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.email = self.data.get('email')
        user.save()
        return user