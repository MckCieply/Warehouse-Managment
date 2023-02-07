from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewUserForm, LoginUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(response):
    return render(response, "management/home.html")

def signup_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/signup.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = LoginUserForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    form = LoginUserForm()
    return render(request = request, template_name = "registration/login.html", context = {"login_form":form})

def logout(response):
    return render(response, "registration/logout.html")

def state(response):
    return render(response, "management/state.html")