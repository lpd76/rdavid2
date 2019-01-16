from django.db import models
from urllib3.util import parse_url


from services.models import Service
from speciality.models import Problematique




# Create your models here.
class Clientele(models.Model):
    nom_fr = models.CharField(max_length=200, unique=True)
    nom_en = models.CharField(max_length=200, blank=True)
    services = models.ManyToManyField(Service, blank=True)
    probleme = models.ManyToManyField(Problematique)
    def __str__(self):
        return self.nom_fr
    class Meta:
        verbose_name_plural = 'clienteles'
        ordering = ['nom_fr']  
    def get_problems(self, Besoin):
        prob = Besoin.objects.all().filter(clientele_type_id=self.id)
        return list(prob)
    
class Ressource(models.Model):
    url = models.URLField()
    nom_fr = models.CharField(max_length=100, blank=True)
    nom_en = models.CharField(max_length=100, blank=True)
    desc_fr = models.TextField(max_length = 500, blank=True)
    desc_en = models.TextField(max_length = 500, blank=True)
   
    
    def get_name(self):
        parseUrl = parse_url(self.url)
        return parseUrl

    def __str__(self):
        return "host : " + self.get_name()[2] + self.get_name()[4]   
    
class Besoin(models.Model):
    clientele_type = models.ForeignKey(Clientele, on_delete=models.CASCADE)
    probleme = models.ForeignKey(Problematique, on_delete=models.CASCADE)
    ressource = models.ManyToManyField(Ressource)
    class Meta:
        unique_together = ("clientele_type", "probleme")
        ordering = ["clientele_type", "probleme"]   
    def __str__(self):
        c = self.clientele_type.nom_fr
        p = self.probleme.nom_fr
        return c + " : " + p
        
