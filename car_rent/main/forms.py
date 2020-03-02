from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MessageStockForm(forms.ModelForm):
    class Meta:
        model = MessageStock
        fields = "__all__"


"""Registration"""
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]