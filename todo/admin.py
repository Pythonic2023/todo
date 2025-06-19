from django.contrib import admin
from .models import Users, TodoList, TodoItem

# Register your models here.
admin.site.register(Users)
admin.site.register(TodoList)
admin.site.register(TodoItem)
