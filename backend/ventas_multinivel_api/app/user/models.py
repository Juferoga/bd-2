from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .managers import UserManager
from .data import *


class User(AbstractUser):
    oracle_password = models.CharField(max_length=30)
    role = models.CharField(max_length=30, choices=ROLES, null=True)
    uid = models.IntegerField()
    objects = UserManager()



    def get_oracle_password(self):
        return self.oracle_password

    def get_role(self):
        return self.role
    
    def get_uid(self):
        return self.uid

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
