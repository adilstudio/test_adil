from django import forms
from .models import Utilisateur, BaseDeDonnees

class UtilisateurCreationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'last_name', 'first_name', 'email', 'password', 'bases_de_donnees']
        labels = {
            'username': 'Nom d\'utilisateur',
            'last_name': 'Nom',
            'first_name': 'Prénom',
            'email': 'Adresse email',
            'password': 'Mot de passe',
            'bases_de_donnees': 'Bases de données'
        }

    bases_de_donnees = forms.ModelMultipleChoiceField(
        queryset=BaseDeDonnees.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class UtilisateurModificationForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'user', 'last_name', 'first_name', 'email', 'password', 'bases_de_donnees']
        labels = {
            'username': 'Nom d\'utilisateur',
            'user': 'Utilisateur',
            'last_name': 'Nom',
            'first_name': 'Prénom',
            'email': 'Adresse email',
            'password': 'Mot de passe',
            'bases_de_donnees': 'Bases de données'
        }

    bases_de_donnees = forms.ModelMultipleChoiceField(
        queryset=BaseDeDonnees.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(UtilisateurModificationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['user'].widget = forms.HiddenInput()
