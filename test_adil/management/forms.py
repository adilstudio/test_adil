from django import forms
from .models import Utilisateur, BaseDeDonnees

class UtilisateurCreationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'adresse_email', 'mot_de_passe', 'bases_de_donnees']

    bases_de_donnees = forms.ModelMultipleChoiceField(
        queryset=BaseDeDonnees.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class UtilisateurModificationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'prenom', 'adresse_email', 'bases_de_donnees']

    bases_de_donnees = forms.ModelMultipleChoiceField(
        queryset=BaseDeDonnees.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
