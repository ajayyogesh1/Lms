from django.urls import path
from . import views
urlpatterns=[path('',views.Info,name="info"),path('InfoAdd',views.InfoAdd,name="info")]