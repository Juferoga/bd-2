from django.urls import path
from .views import LogIn

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', LogIn.as_view(), name='authentication'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]