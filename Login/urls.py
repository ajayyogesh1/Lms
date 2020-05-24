from django.urls import path
from . import views
urlpatterns=[path('',views.Login,name="login"),
				path('LoginValidate',views.LoginCheck,name="login"),
				path('Forgot',views.Forgot,name="Forgot")]
