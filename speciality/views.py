from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import ProblematiqueType,Problematique
from services.models import Service
from psychologues.models import Psychologue
from clientele.models import Clientele, Besoin
from orientation.models import Orientation
from SectionText.models import SectionText
from django.contrib.auth.models import User


# Create your views here.
def speciality_list(request):
    services = get_list_or_404(Service)
    speciality_list = get_list_or_404(ProblematiqueType)
    psychologues = Psychologue.objects.all()
    all_clientele = get_list_or_404(Clientele)
    orientations = get_list_or_404(Orientation)
    sectiontext= get_list_or_404(SectionText)
    
    specialities = {}
    for item in speciality_list:
        specialities[item] = Problematique.objects.filter(Type_de_Problematique=item).order_by('nom_fr')
          
    list_of_psy = []
    for psychologue in psychologues:
        list_of_psy.append(get_object_or_404(User, id=psychologue.user_id))
    list_of_psy
    
    probleme_clientele = {}
    for c in all_clientele:
        if c.get_problems(Besoin):
            probleme_clientele[c.nom_fr] = c.get_problems(Besoin)
    
    context = {'specialities':specialities, 'services':services, 'staff':list_of_psy, 'all_clientele':all_clientele, 'orientations':orientations, 'sectiontext':sectiontext, 'probleme_clientele':probleme_clientele }
        
    return render(request, 'speciality/specialities.html', context)
