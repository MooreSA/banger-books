from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

# Create your views here.
class Login_form(forms.Form):
    username = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password'}))

class Register_form(forms.Form):
    username = forms.CharField(max_length=191, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))

@login_required()
def index(request):
    #If user is logged in, display info on user
    return render(request, "users/user.html")


def login_view(request):
    #If user is logged in, redirect to userinfo
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    #If user submits form, authenticate credentials
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        #user returns None with invalid credentials
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))

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
    #Logs user out
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged Out",
        "form": Login_form
    })

def register(request):
    #If user is already logged in, doesn't allow them to register new acct
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    #TODO Confirm that username/email are unique
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
        return HttpResponseRedirect(reverse("users:index"))

    #User sees page first time
    return render(request, "users/register.html", {
        "form": Register_form(),
    })
