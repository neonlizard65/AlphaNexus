from django.urls import path
from . import views

urlpatterns = [
    path("countries", views.getCountries),
    path("users", views.getUsers),
] 