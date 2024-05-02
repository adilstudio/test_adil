from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

#Model pour les données de revues
class BaseDeDonnees(models.Model):
    NOM_CHOICES = [
        ('Scopus', 'Scopus'),
        ('PubMed', 'PubMed'),
        ('Dimensions', 'Dimensions'),
        ('Web of Science', 'Web of Science'),
    ]
    nom = models.CharField(max_length=100, choices=NOM_CHOICES)

    def __str__(self):
        return self.nom

#Model pour les utilisateurs avec la jointure ManyToMany et sécurité minimale demandée du hashage du mot de passe
class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100) #mot de passe à hasher avant l'envoi à la bd
    bases_de_donnees = models.ManyToManyField(BaseDeDonnees)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
