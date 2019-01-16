from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Psychologue, Competence
from django.contrib.auth.models import User

# Create your views here.

def psychologues_profile(request, pk):
    psychologue_info = get_object_or_404(Psychologue, pk=pk)
    user_info = get_object_or_404(User, pk=psychologue_info.user_id)
    services = psychologue_info.get_services_by_clientele_type()
    
    try:
        competence_liste = Competence.objects.filter(psychologue_id=pk)
    except Competence.DoesNotExist:
        competence_liste=[]
    context = {'psy': psychologue_info, 'user': user_info, 'services':services}
    return render(request, 'psychologues/psy_profile.html', context)

def psychologue_competences(request, pk):
    competence = get_object_or_404(Competence, id=pk)
    context = {'competence':competence}
    return render(request, 'psychologues/psy_competences.html', context)