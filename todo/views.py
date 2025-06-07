from django.shortcuts import get_object_or_404, render, redirect
from .models import User

# Create your views here.

def index(request):
	return render(request, "todo/index.html")

def signup(request):
	if request.method == "GET":
		return render(request, "todo/signup.html")
	else:
		first_name = request.POST.get("first")		
	    last_name = request.POST.get("last")
		
		if first_name && last_name:
			User.objects.create(first_name = first_name, last_name = last_name)
		return redirect("todo:index.html")

def signin(request):
	return render(request, "todo/signin.html")
