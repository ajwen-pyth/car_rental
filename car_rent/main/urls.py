from django.urls import path
from .views import *

urlpatterns = [
    path("", startpage_response, name="start_page"),
    path("carslist", carlistpage_response, name="cars_list"),
    path("contact", contactpage_response, name="contact_form"),
    path("messages", messagelist_response, name="message_list"),
    path("messageadd", messageadd_response, name="message_add")
    ]