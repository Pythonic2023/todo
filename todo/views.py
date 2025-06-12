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
			username = form.cleaned_data['username']
			user = form.save()
			return signupsuccess(request, username)
		else:
			messages.error(request, "Registration failed. Please correct the errors below")
			print(form.errors)
			return signuperror(request)
	else:
		form = UserCreationForm()
	return render(request, "todo/signup.html", {"form": form})

def signupsuccess(request, user):
	username = user
	context = {'username': username}
	return render(request, "todo/signupsuccess.html", context)

def signuperror(request):
	error_message = "Sign up failed"
	context = {'error_message': error_message}
	return render(request, "todo/signuperror.html", context)
	
	

def signin(request):
	return render(request, "todo/signin.html")
