from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.
class Login_form(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

class Register_form(forms.Form):
    username = forms.CharField(max_length=191)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first = forms.CharField(max_length=30)
    last = forms.CharField(max_length=150)

def index(request):
    #If user is logged in, display info
    if request.user.is_authenticated:
        return render(request, "users/user.html")

    #Else redirect to login page
    return HttpResponseRedirect(reverse("login"))


def login_view(request):
    #If user is logged in, redirect to userinfo
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    #If user submits form, authenticate credentials
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        #user returns None with invalid credentials
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))

        #Prompts user to try again if invalid
        return render(request, "users/login.html",{
            "form": Login_form,
            "message": "Invalid Credentials"
        })

    #Default View
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
    #If user is already logged in, doesn't allow them to register new acct
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    
    #If user submits form
    if request.method == "POST":
        form = Register_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]
            first = form.cleaned_data["first"]
            last = form.cleaned_data["last"]
        if password != confirm_password:
            return render(request, "users/register.html", {
                "form": Register_form(),
                "message": "Passwords must match"
            })
        user = User.objects.create_user(username=username, email=email, password=password, first_name=first, last_name=last)
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    #User sees page first time
    return render(request, "users/register.html", {
        "form": Register_form(),
        "message": "TODO"
    })
