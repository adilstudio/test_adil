from django import forms
from .models import Utilisateur

class UtilisateurCreationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'adresse_email', 'mot_de_passe', 'bases_de_donnees']

    BASES_CHOICES = [
        ('Scopus', 'Scopus'),
        ('PubMed', 'PubMed'),
        ('Dimensions', 'Dimensions'),
        ('Web of Science', 'Web of Science'),
    ]

    bases_de_donnees = forms.MultipleChoiceField(
        choices=BASES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class UtilisateurModificationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'adresse_email', 'bases_de_donnees']

    BASES_CHOICES = [
        ('Scopus', 'Scopus'),
        ('PubMed', 'PubMed'),
        ('Dimensions', 'Dimensions'),
        ('Web of Science', 'Web of Science'),
    ]

    bases_de_donnees = forms.MultipleChoiceField(
        choices=BASES_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
