from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views #domyślne widoki na potrzeby logowania
from django.conf.urls import url


urlpatterns = [
    path("", startpage_response, name="start_page"),
    path("carslist", carlistpage_response, name="cars_list"),
    path("contact", contactpage_response, name="contact_form"),
    path("messages", messagelist_response, name="message_list"),
    path("messageadd", messageadd_response, name="message_add"),
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("register", signup_view_response, name="register"),
    path("logout-done", logout_done)
    ]