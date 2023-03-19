from django.urls import path
from .views import UserLogin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns=[
    path('auth/', UserLogin.as_view(), name='users_login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),# plus jaja
]