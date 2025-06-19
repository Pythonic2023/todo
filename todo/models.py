from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import models
from django.template.context_processors import request


# Create your models here.
class Users(models.Model):
	first_name = models.CharField(max_length=15)
	last_name = models.CharField(max_length=15)
	password = models.CharField(max_length=30)
	def __str__(self):
		full_name = [self.first_name, self.last_name]
		return " ".join(full_name)
	class Meta:
		verbose_name_plural = "User"


class TodoList(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	todo_title = models.CharField(max_length=100)
	def __str__(self):
		return self.todo_title


class TodoItem(models.Model):
	list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")
	todo_item = models.CharField(max_length=100)
	def __str__(self):
		return self.todo_item

