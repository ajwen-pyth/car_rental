from django import forms
from .models import *


class MessageStockForm(forms.ModelForm):
    class Meta:
        model = MessageStock
        fields = "__all__"
