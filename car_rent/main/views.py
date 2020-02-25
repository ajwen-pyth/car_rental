from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, Http404
from .models import *
from .forms import *

# Create your views here.

def startpage_response(request):
    return render(request, "start.html")

"""Available car list"""
def carlistpage_response(request):
    all_cars = CarStock.objects.all()
    return render(request, "cars-list.html", {"cars": all_cars})

"""Available messages list"""
def messagelist_response(request):
    all_message = MessageStock.objects.all()
    return render(request, "message-list.html", {"messages": all_message})

"""Contact form"""
def contactpage_response(request):
    return render(request, "contact.html")

"""Send a message from contact form into database"""
def messageadd_response(request):
    form = MessageStockForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("start_page")
    return render(request, "message-add.html", {"form": form})
