from django.db import models

# Create your models here.
class Orientation(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, blank=True)
    desc_fr = models.TextField(max_length=1000, blank=True)
    desc_ang = models.TextField(max_length=1000, blank=True)
    
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name_plural = 'Orientations'
        ordering = ['nom']