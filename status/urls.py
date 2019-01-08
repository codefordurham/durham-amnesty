from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('<str:driver_license_number>/records', views.records, name='records'),
]