from django import forms 
from todo.models import Users

class NameForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ["first_name", "last_name", "password"]
		widgets = {
			'password': forms.PasswordInput(),
		}
