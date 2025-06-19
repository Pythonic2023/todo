from urllib.request import Request

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from todo.forms import TodoListForm, TodoItemForm
from todo.models import TodoList, TodoItem


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
			signup_error = form.errors
			return error(request, signup_error)
	else:
		form = UserCreationForm()
	return render(request, "todo/signup.html", {"form": form})

def signupsuccess(request, user):
	username = user
	context = {'username': username}
	return render(request, "todo/signupsuccess.html", context)

def error(request, error):
	context = {'error': error}
	return render(request, "todo/error.html", context)
	
def signin(request):
	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/todo/')
		else:
			signin_error = "Retry username and password"
			return error(request, signin_error)
	else: 
		form = AuthenticationForm()
	return render(request, "todo/signin.html", {'form': form})


@login_required
def todo_list(request, username):
	if request.method == "POST":
		list_name = TodoListForm(request.POST)
		if list_name.is_valid():
			list_name_instance = list_name.save(commit=False)
			list_name_instance.user = request.user
			list_name_instance.save()
			return redirect(reverse("todo:index"))
		else:
			list_error = list_name.errors
			return error(request, list_error)
	else:
		list_name = TodoListForm

	return render(request, "todo/todolist.html", {'list_name':list_name})


@login_required
def create_item(request):
	todo_list_object = TodoList.objects.get(user=request.user)
	if request.method == "POST":
		item_name = TodoItemForm(request.POST)
		if item_name.is_valid():
			item_name_instance = item_name.save(commit=False)
			item_name_instance.list = todo_list_object
			item_name_instance.save()
			return redirect(reverse("todo:index"))
		else:
			item_error = item_name.errors
			return error(request, item_error)
	else:
		existing_items = todo_list_object.items.all()
		item_name = TodoItemForm()
		context = {
			'item_name': item_name,
			'todo_list_object': todo_list_object,
			'existing_items': existing_items,

		}
	return render(request, "todo/additem.html", context)