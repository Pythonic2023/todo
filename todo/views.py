from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import User
from .forms import NameForm

# Create your views here.

def index(request):
	return render(request, "todo/index.html")

def signup(request):
	if request.method == "GET":
		form = NameForm()
	else:
		form = NameForm(request.POST)			
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/todo")
	return render(request, "todo/signup.html", {"form": form})

def signin(request):
	return render(request, "todo/signin.html")
