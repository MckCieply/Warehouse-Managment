from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import NewUserForm, LoginUserForm, UpdateForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Item, Stock
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
    items = Item.objects.all()
    return render(response, "management/state.html", {"items": items})

def update(request, id):
    items = Item.objects.get(item_id=id)
    stock = Stock.objects.get(item_id=id)
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            stock.stock_state += form.cleaned_data['stock_state']
            stock.save(update_fields=["stock_state"])
            return redirect("state")
    else:
        form = UpdateForm(request.POST)
    return render(request, template_name="management/update.html",context={'items': items, 'stock':stock,'update_form':form,})