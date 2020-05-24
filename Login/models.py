from django.db import models
class Student(models.Model):
	Name=models.CharField(max_length=100)
	Class=models.CharField(max_length=2)
	Email=models.EmailField(max_length=100,unique=True)
	Password=models.CharField(max_length=100,unique=True)
	PhoneNumber=models.CharField(max_length=10,unique=True)
	is_Active=models.BooleanField(default=False)
	def __str__(self):
		return self.Name