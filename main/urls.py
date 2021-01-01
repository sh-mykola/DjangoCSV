from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("schemas/", views.schemas, name="schemas"),
    path("schemas/delete/<int:id>", views.schemas_delete, name="schemas_delete"),
    path("schemas/new/", views.schemas_new, name="schemas_new"),
]