from django.urls import path

from . import views

urlpatterns = [
    path('clientele/<int:pk>/', views.detail_problematique, name='detail_problematique'),
    
]