from django.shortcuts import render,redirect
from Login.models import Student
from HomePage.models import Class as Std
from HomePage.models import Subject
from HomePage.models import Material
from django.views.decorators.cache import never_cache
@never_cache
def Home(request,id):
	Name,Dates=Student.objects.get(pk=id),{}
	try:
		Info_About_Class=Std.objects.get(Class_Name="Class_"+str(Name.Class))
		Info_About_Class_Subject=Subject.objects.filter(key_id=Info_About_Class)
		Info_About_Class=Info_About_Class.Class_Name.replace('_',' ')
		Info_About_Class_Subject_Material_Latest=Material.objects.all().order_by('-id')[:3]
	except:
		Info_About_Class="Class %s"%(Name.Class)
		Info_About_Class_Subject={}
		Info_About_Class_Subject_Material={}
	if Name.is_Active:
		return render(request,"Home.html",{"UserName":Name,"ClassInfo":Info_About_Class,"SubjectInfo":Info_About_Class_Subject,"MaterialInfo":Info_About_Class_Subject_Material_Latest})
	else:return redirect('/login')
def Course(request,id,id2):
	Name=Student.objects.get(pk=id)
	Info_About_Class_Subject=Subject.objects.get(pk=id2)
	try:
		Info_About_Class_Subject_Material=Material.objects.filter(key_id=id2)
	except:
		Info_About_Class_Subject_Material={}
	return render(request,"Course.html",{"UserName":Name,"ClassInfo":"Class %s"%(Name.Class),"SubjectInfo":Info_About_Class_Subject,"MaterialInfo":Info_About_Class_Subject_Material})
@never_cache
def Logout(request,id,id2=0):
	Name=Student.objects.get(pk=id)
	Name.is_Active=0
	Name.save()
	return redirect('/login')