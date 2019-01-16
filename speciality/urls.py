from django.urls import path
from . import views

urlpatterns = [
    path('index', views.speciality_list, name='speciality_list'),
]