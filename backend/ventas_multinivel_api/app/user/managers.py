from django.contrib.auth.models import BaseUserManager
from .data import ADMINISTRATOR

class UserManager(BaseUserManager):
  use_in_migrations = True

  def _create_user(self, username, password, oracle_password, role, uid, **kwargs):
    user = self.model(username=username, oracle_password=oracle_password, role=role, uid=uid, **kwargs)
    user.set_password(password)
    setattr(user, 'role', role)
    setattr(user, 'uid', uid)
    user.save()
    return user

  def create_user(self, username, password=None, oracle_password=None, role=None, uid=None, **kwargs):
    kwargs.setdefault('is_superuser', False)
    return self._create_user(username, password, oracle_password, role , uid, **kwargs)

  def create_superuser(self, username, password, **kwargs): #,oracle_password, role, uid, **kwargs):
    kwargs.setdefault('is_superuser', True)
    kwargs.setdefault("is_staff", True)
    kwargs.setdefault("oracle_password",password)
    kwargs.setdefault("role", ADMINISTRATOR)
    kwargs.setdefault("uid", 80)
    return self._create_user(username, password, **kwargs)