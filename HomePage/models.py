from django.db import models
class Class(models.Model):
	Class_Choices=(('Class_1','Class 1'),('Class_2','Class 2'),('Class_3','Class 3'),('Class_4','Class 4'),('Class_5','Class 5'),('Class_6','Class 6'),('Class_7','Class 7'),('Class_8','Class 8'),('Class_9','Class 9'),('Class_10','Class 10'),('Class_11','Class 11'),('Class_12','Class 12'))
	Class_Name=models.CharField(max_length=10,choices=Class_Choices,default='Class_12',unique=True)
	def __str__(self):
		return self.Class_Name
	class Meta:
		verbose_name_plural= "Classes"
class Subject(models.Model):
	Subject_Name=models.CharField(max_length=50,unique=True)
	Staff_Name=models.CharField(max_length=50)
	Subject_Image=models.ImageField(upload_to="ClassImages/")
	Description=models.TextField()
	key=models.ForeignKey(Class,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.key)+" / "+self.Subject_Name
class Material(models.Model):
	Material_Name=models.CharField(max_length=50,unique=True)
	Upload_Date=models.DateTimeField(auto_now=True)
	Material=models.FileField(upload_to="Documents/")
	key=models.ForeignKey(Subject,on_delete=models.CASCADE)
	def __str__(self):
		return str(self.key)+" / "+self.Material_Name
