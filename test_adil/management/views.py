from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Utilisateur

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UtilisateurCreationForm, UtilisateurModificationForm

def page_accueil(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            nom_utilisateur = form.cleaned_data.get('username')
            mot_de_passe = form.cleaned_data.get('password')
            utilisateur = authenticate(username=nom_utilisateur, password=mot_de_passe)
            if utilisateur is not None:
                login(request, utilisateur)
                return redirect('liste_utilisateurs')
    else:
        form = AuthenticationForm()
    return render(request, 'page_accueil.html', {'form': form})

def liste_utilisateurs(request):
    if not request.user.is_authenticated:
        return redirect('page_accueil')
    utilisateurs = Utilisateur.objects.all()
    return render(request, 'liste_utilisateurs.html', {'utilisateurs': utilisateurs})

# Vue pour créer un utilisateur
def creer_utilisateur(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilisateur créé avec succès.')
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurCreationForm()
    return render(request, 'creer_utilisateur.html', {'form': form})

# Vue pour modifier un utilisateur
def modifier_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, pk=utilisateur_id)
    if request.method == 'POST':
        form = UtilisateurModificationForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilisateur modifié avec succès.')
            return redirect('liste_utilisateurs')
    else:
        form = UtilisateurModificationForm(instance=utilisateur)
    return render(request, 'modifier_utilisateur.html', {'form': form})

# Vue pour supprimer un utilisateur
def supprimer_utilisateur(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, pk=utilisateur_id)
    if request.method == 'POST':
        utilisateur.delete()
        messages.success(request, 'Utilisateur supprimé avec succès.')
        return redirect('liste_utilisateurs')
    return render(request, 'supprimer_utilisateur.html', {'utilisateur': utilisateur})
