from django.urls import path

from . import views

urlpatterns = [
    path('psychologues/<int:pk>/', views.psychologues_profile, name='psychologues_profile'),
    path('psychologues/competence/<int:pk>/', views.psychologue_competences, name='psychologue_competences'),
]