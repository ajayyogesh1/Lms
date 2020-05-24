from django.shortcuts import render,redirect
from .models import Student
from django.http import HttpResponse as Response
def Login(request):
	return render(request,"Login.html")
def LoginCheck(request):
	Id,Password=request.POST["email"],request.POST["pass"]
	Check=Student.objects.filter(Email=Id) and Student.objects.filter(Password=Password)
	if Check:
		id=Check[0].id
		Check=Student.objects.get(pk=id)
		Check.is_Active=1
		Check.save()
		return redirect('/homepage/'+str(id),id=id)
	else:
		return redirect('/login/')
def Forgot(request):
	return Response("<h1><b>Page 404 Not Found</h1></b><br>The Email Service is Under Development<br>Sorry for the Inconvenience")