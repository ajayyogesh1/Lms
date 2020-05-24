from django.shortcuts import render,redirect
from .models import Information
def Info(request):
	return render(request,"Info.html")
def InfoAdd(request):
	Info=Information.objects.create(Name=request.POST["name"],Email=request.POST["email"])
	Info.save()
	print(request.POST["name"],request.POST["email"])
	return redirect('/login')