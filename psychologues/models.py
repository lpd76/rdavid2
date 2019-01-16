from django.db import models
from django.contrib.auth.models import User
from speciality.models import Problematique
from services.models import Service
from clientele.models import Besoin
from orientation.models import Orientation
# Create your models here.
class Psychologue(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to = 'static/media/')
    phone = models.CharField(max_length=10, blank=True)
    fax = models.CharField(max_length=10, blank=True)
    bio = models.TextField(max_length=1700, blank=True)
    education = models.CharField(max_length=70, blank=True)
    site_web = models.URLField(blank=True)
    linked_in = models.URLField(blank=True)
    
    def __str__(self):
        user_info = User.objects.get(id=self.user_id)
        return user_info.first_name + ' ' + user_info.last_name
    class Meta:
        ordering = ['user']
        
    def get_services_by_clientele_type(self):
        if Competence.objects.filter(psychologue__id=self.pk).exists():
            competences = Competence.objects.filter(psychologue__id=self.pk)
            comp = {}
            for clientele in competences:
                services = []
                for service in competences:
                    if service.besoin.clientele_type.id == clientele.besoin.clientele_type.id:
                        services.append((service.id, service.besoin.probleme.nom_fr))
                comp[clientele.besoin.clientele_type.nom_fr] = services
        else:
            comp= {}
        return comp
    
class Competence(models.Model):
    psychologue = models.ForeignKey(Psychologue, on_delete=models.CASCADE)
    besoin = models.ForeignKey(Besoin, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    orientation = models.ForeignKey(Orientation, on_delete=models.CASCADE, blank=True)
    desc_fr = models.TextField(max_length=1000, blank=True)
    desc_ang = models.TextField(max_length=1000, blank=True)
    charge = models.FloatField(blank=True)
    
    def __str__(self):
        user_info = User.objects.get(id=self.psychologue.user_id)
        p = user_info.first_name + ' ' + user_info.last_name
        b = self.besoin.clientele_type.nom_fr
        c = self.besoin.probleme.nom_fr
        s = self.service.nom
        return p + " -> " + s + " pour " + c + " chez " + b  
    
    class Meta:
        ordering = ['psychologue', 'besoin', 'service']