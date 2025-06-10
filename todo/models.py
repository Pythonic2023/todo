from django.db import models

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
