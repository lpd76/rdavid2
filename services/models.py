from django.db import models

# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200, blank=True)
    url_fr = models.URLField(max_length=200, blank=True)
    url_en = models.URLField(max_length=200, blank=True)
       
    class Meta:
        verbose_name_plural = 'Services'
        ordering = ['nom']
    def __str__(self):
        return self.nom