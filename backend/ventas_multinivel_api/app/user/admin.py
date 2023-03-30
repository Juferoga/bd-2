from django.contrib import admin
from app.user.models import User
from django.contrib.auth import get_user_model
@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
  readonly_fields = ('email', 'username')
  list_display = ('username', 'role', 'oracle_password', 'is_superuser', 'is_staff')
  fieldsets = (
    (
      'Información básica', 
      {
        'fields': ('username', 'email', 'password', 'role', 'uid')
      }
    ),
    (
      'Información específica', 
      {
        'fields': (('first_name', 'last_name'), ('oracle_password', 'is_superuser', 'is_staff'))
      }
    )
  )
  list_filter = ('is_active', 'role')
  search_fields = [
    'username',
    'first_name',
    'last_name'
  ]
  search_fields = [
    'username',
  ]
