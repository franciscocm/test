from django.urls import path

from . import views

urlpatterns = [
    path("register_client", views.register_client, name="register_client"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout")
]