from django.urls import path
from .views import createUserView, allUsersView

urlpatterns = [
    path('add/', createUserView.as_view(), name='createUserView'),
    path("users/all/", allUsersView.as_view(), name="AllUsersView")
]