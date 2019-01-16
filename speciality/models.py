from django.db import models

# Create your models here.
class ProblematiqueType(models.Model):
    nom_fr = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=1000)
    
    class Meta:
        verbose_name_plural = 'Type de Problématique'
        ordering = ['nom_fr']
    
    def __str__(self):
        return self.nom_fr
    
class Problematique(models.Model):
    Type_de_Problematique = models.ForeignKey(ProblematiqueType, on_delete=models.CASCADE)
    nom_fr = models.CharField(max_length=200, unique=True)
    desc_fr = models.TextField(default=None, blank=True)
    
    class Meta:
        verbose_name_plural = 'Problematiques'
        ordering = ['nom_fr']
    
    def __str__(self):
        return self.nom_fr
    