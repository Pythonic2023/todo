from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.

def index(request):
	return render(request, "todo/index.html")

def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, f"Welcome, {user.username}! Your account has been successfully created.")
			return redirect(reverse("todo:index"))
		else:
			messages.error(request, "Registration failed. Please correct the errors below")
	else:
		form = UserCreationForm()
		return render(request, "todo/signup.html", {"form": form})

def signin(request):
	return render(request, "todo/signin.html")
