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
    path("wishlist", views.wishlist, name="wishlist"),
    path("cart", views.cart, name="cart"),
    path("change_product/<int:id>", views.change_product, name="change_product"),
    path("users/<int:id>", views.users, name="users"),
    path("create_product", views.create_product, name="create_product"),
    path("create_developer", views.create_developer, name="create_developer"),
    path("developer/<int:id>", views.developer_games, name="developer_games"),
    
]

