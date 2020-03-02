from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponse, Http404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


# Create your views here.


def startpage_response(request):
    return render(request, "start.html")


"""Register of user """
def signup_view_response(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect("start_page")
    return render(request, 'register.html', {"form": form})

"""Available car list"""
@login_required()
def carlistpage_response(request):
    all_cars = CarStock.objects.all()
    return render(request, "cars-list.html", {"cars": all_cars})


"""Available messages list"""
@login_required()
def messagelist_response(request):
    all_message = MessageStock.objects.all()
    return render(request, "message-list.html", {"messages": all_message})


"""Contact form"""
@login_required()
def contactpage_response(request):
    return render(request, "contact.html")


"""Send a message from contact form into database"""
@login_required()
def messageadd_response(request):
    form = MessageStockForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("start_page")
    return render(request, "message-add.html", {"form": form})


"""Import action"""
@login_required()
def import_response(request):
    pass


"""Logout done"""
def logout_done(request):
    return render(request, "logout-done.html")