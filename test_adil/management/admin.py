from django.contrib import admin

from management.models import BaseDeDonnees
from management.models import Utilisateur

admin.site.register(BaseDeDonnees)
admin.site.register(Utilisateur)
