from django.shortcuts import render
from .models import Besoin
from psychologues.models import Psychologue, Competence

# Create your views here.

def detail_problematique(request, pk):
    besoins_detail = Besoin.objects.get(id=pk)
    qui_offre_le_service = Competence.objects.filter(besoin=pk)
    context = {'besoins_detail':besoins_detail, 'psy':qui_offre_le_service}
    return render(request, 'clientele/besoin_detail.html', context)