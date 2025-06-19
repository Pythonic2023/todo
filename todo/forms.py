from django import forms 
from todo.models import Users, TodoList, TodoItem

class NameForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ["first_name", "last_name", "password"]
		widgets = {
			'password': forms.PasswordInput(),
		}

class TodoListForm(forms.ModelForm):
	class Meta:
		model = TodoList
		fields = ["todo_title"]

class TodoItemForm(forms.ModelForm):
	class Meta:
		model = TodoItem
		fields = ["todo_item"]