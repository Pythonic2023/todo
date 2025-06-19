from django.urls import path
from . import views

app_name = "todo"
urlpatterns = [
	path("", views.index, name="index"),
	path("signup/", views.signup, name="signup"),
	path("signup/signupsuccess/", views.signupsuccess, name="signupsuccess"),
	path("error/", views.error, name="error"),
	path("signin/", views.signin, name="signin"),
	path("todolist/<str:username>", views.todo_list, name="todolist"),
	path("additem/", views.create_item, name="additem")
]
