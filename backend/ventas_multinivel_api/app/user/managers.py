from django.contrib.auth.models import BaseUserManager
from .data import ADMINISTRATOR

class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, username, password, oracle_password, role, **kwargs):
    user = self.model(username=username,oracle_password=oracle_password,role=role, **kwargs)
    user.set_password(password)
    user.save()
    return user

  def create_user(self, username, password=None, oracle_password=None, role=None, **kwargs):
    kwargs.setdefault('is_superuser', False)
    return self._create_user(username, password, oracle_password, **kwargs)

  def create_superuser(self, username, password, oracle_password, role,**kwargs):
    kwargs.setdefault('is_superuser', True)
    kwargs.setdefault("is_staff", True)
    kwargs.setdefault("oracle_password",oracle_password)
    kwargs.setdefault(ADMINISTRATOR, role)
    return self._create_user(username, password,oracle_password,**kwargs)