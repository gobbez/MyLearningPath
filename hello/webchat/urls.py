from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("", views.webchat, name="webchat"),
    path("login/", LoginView.as_view(template_name="webchat/login.html"), name="login"),
]