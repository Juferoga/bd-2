from django.urls import path
from .views import createUserView

urlpatterns = [
    path('', createUserView.as_view(), name='createUserView'),
]