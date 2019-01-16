from django.contrib import admin
from .models import Clientele, Besoin, Ressource

# Register your models here.
admin.site.register(Clientele)
admin.site.register(Besoin)
admin.site.register(Ressource)
