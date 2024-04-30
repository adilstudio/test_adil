from django.db import models

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
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse_email = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=100)  #mot de passe à hasher avant l'envoi à la bd
    bases_de_donnees = models.ManyToManyField(BaseDeDonnees)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
