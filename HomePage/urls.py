from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[path('<int:id>/',views.Home,name="Home"),path('<int:id>/<int:id2>/',views.Course,name="Course"),path('<int:id>/logout/',views.Logout,name="Logout"),path('<int:id>/<int:id2>/logout/',views.Logout,name="Logout")]