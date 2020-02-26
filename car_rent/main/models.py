from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.


class CarStock(models.Model):
    model = models.CharField(max_length=15)
    year = models.CharField(null=True, blank=True, max_length=4)
    eng_cap = models.CharField(max_length=4, null=True, blank=True)
    description = models.TextField(default="")
    photo = models.ImageField(null=True, blank=True)
    segment = models.ManyToManyField('Segment', related_name="car_segment")
    price = models.CharField(max_length=4, null=True, blank=True)

    def __str__(self):  # dzieki temu w panelu adm. wyswietlaja sie pelne nazwy dodanych aut
        return f"{self.model} - {self.year}"

    class Meta:
        verbose_name = "samochód"
        verbose_name_plural = "samochody"


class MessageStock(models.Model):
    name = models.CharField(max_length=15, null=True, blank=True)
    surname = models.CharField(max_length=20, null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=12, blank=True)  # validators should be a list
    email = models.EmailField(help_text="A valid email please")
    message = models.TextField(default="")
    mess_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.mess_date}"

    class Meta:
        verbose_name = "wiadomość"
        verbose_name_plural = "wiadomości"


class Segment(models.Model):
    segment = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.segment}"
