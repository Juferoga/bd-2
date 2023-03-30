from django.urls import path
from .views import createUserView

urlpatterns = [
    path('add/', createUserView.as_view(), name='createUserView'),
]