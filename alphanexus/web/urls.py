from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="home"),
    path("about", views.about, name="about"),
    path("register", views.register, name="register"),
    path("login", views.user_login, name="login"),
    path("logout", views.user_logout, name="logout"),
    path("change_pass", views.change_password, name="change_pass"),
    path("change_user", views.change_user, name="change_user"),
    path("cabinet", views.cabinet, name="cabinet"),
    path("developer", views.developer, name="developer"),
    path("library", views.library, name="library"),
    path("store", views.store, name="store"),
    
    
]

