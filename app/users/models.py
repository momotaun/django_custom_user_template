from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import(
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(
        self,
        email,
        password,
        **extra_fields):
        if not email:
            raise ValueError('Valid email must be set.')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
            )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        email,
        password,
        **extra_fields):
        extra_fields.setdefault('is_verified', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        self.create_user(email, password, **extra_fields)
        


class User(AbstractBaseUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(verbose_name=("E-mail"), unique=True, max_length=254)
    is_verified = models.BooleanField(verbose_name=("Verified"), default=False)
    is_active = models.BooleanField(verbose_name=("Active"), default=False)
    is_staff = models.BooleanField(verbose_name=("Staff"), default=False)
    created_at = models.DateTimeField(verbose_name=("Created at"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=("Updated at"), auto_now=True, auto_now_add=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access':str(refresh.access_token)
        }