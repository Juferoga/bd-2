from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class User(AbstractUser):
    oracle_password = models.CharField(max_length=30)

    def get_oracle_password(self):
        return self.oracle_password