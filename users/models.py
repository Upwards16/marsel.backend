from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from .managers import CustomUserManager


class Position(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(
        max_length=255, null=True, blank=True
    )
    
    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=255)


class User(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateField(blank=True, null=True)
    date_start_work = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    github = models.CharField(max_length=255, null=True)
    linkedin = models.CharField(max_length=255, null=True)
    telegram = models.CharField(max_length=255, null=True)
    chat_id = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=255, null=True)
    salary = models.FloatField(default=0)
    hourly_payment_cost = models.FloatField(default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    cv = models.FileField(
        upload_to='media/cv/', null=True,
        max_length=500
    )
    bank_details = models.CharField(max_length=255, null=True)
    status = models.ForeignKey(
        Status,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="user"
    )
    position = models.ForeignKey(
        Position,
        null=True,
        on_delete=models.DO_NOTHING,
        related_name="user"
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def fullname(self):
        return f'{self.firstname} {self.lastname}'
