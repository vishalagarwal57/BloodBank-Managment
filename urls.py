from django.urls import path
from . import views

urlpatterns = [
    path("",views.main, name="home"),
    path("register/", views.register, name="register"),
    path("donate/", views.donate, name="donate"),
    path("gethelp/", views.gethelp, name="gethelp"),
]