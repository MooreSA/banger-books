from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.
class Login_form(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

def index(request):
    return render(request, "users/user.html")


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        return render(request, "users/login.html",{
            "form": Login_form,
            "message": "Invalid Credentials"
        })

    return render(request, "users/login.html", {
        "form": Login_form()
    })

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out",
        "form": Login_form
    })

def register(request):
    return render(request, "users/register.html")
