from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(CarStock)
admin.site.register(Segment)


@admin.register(CarStock)
class CarStockAdmin(admin.ModelAdmin):
    cars_display = ('model', 'year', 'eng_cap', 'price')
    cars_filter = ('year', 'price')
    search_fields = ('model', 'description')


# admin.site.register(MessageStock)
@admin.register(MessageStock)
class MessageStockAdmin(admin.ModelAdmin):
    message_display = ('name', 'surname', 'phone_number', 'email', 'message', 'mess_date')
    message_filter = ('name', 'surname', 'phone_number', 'email', 'message', 'mess_date')
    message_fields = ('name', 'surname', 'phone_number', 'email', 'message', 'mess_date')

