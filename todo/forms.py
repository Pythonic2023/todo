from django import forms 
from todo.models import User

class NameForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name", "last_name"]
