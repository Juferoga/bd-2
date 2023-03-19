from django.urls import path
from .views import Authentication

from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', Authentication.as_view(), name='authentication'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]