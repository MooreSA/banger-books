from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.
class Login_form(forms.Form):
    username = forms.CharField(max_length=64)
    password = forms.CharField(widget=forms.PasswordInput)

class Register_form(forms.Form):
    username = forms.CharField(max_length=64)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    first = forms.CharField(max_length=64)
    last = forms.CharField(max_length=64)

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
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        first = request.POST["first"]
        last = request.POST["last"]
        if password != confirm_password:
            return render(request, "users/register.html", {
                "form": Register_form(),
                "message": "Passwords must match"
            })

    #User sees page first time
    return render(request, "users/register.html", {
        "form": Register_form(),
        "message": "TODO"
    })
