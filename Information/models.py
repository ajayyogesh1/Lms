from django.db import models
class Information(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.EmailField(max_length=50)
	def __str__(self):
		return "%s / %s"%(self.Name,self.Email)