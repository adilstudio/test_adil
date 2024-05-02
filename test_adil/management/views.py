from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UtilisateurCreationForm, UtilisateurModificationForm
from .models import Utilisateur
from django.db import transaction


def page_accueil(request):
    if request.user.is_authenticated:
        return redirect('liste_utilisateurs')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            nom_utilisateur = form.cleaned_data.get('username')
            mot_de_passe = form.cleaned_data.get('password')
            utilisateur = authenticate(username=nom_utilisateur, password=mot_de_passe)
            if utilisateur is not None:
                login(request, utilisateur)
                messages.success(request, "Vous êtes identifié(e) avec succès!")
                return redirect('liste_utilisateurs')
            else:
                messages.error(request, "Identifiants invalides!")
        else:
            messages.error(request, "Identifiants invalides!")
    else:
        messages.info(request, "Saisir les identifiants!")
        form = AuthenticationForm()
    return render(request, 'page_accueil.html', {'form': form})

def liste_utilisateurs(request):
    if not request.user.is_authenticated:
        return redirect('page_accueil')
    utilisateurs = User.objects.all()
    return render(request, 'liste_utilisateurs.html', {'utilisateurs': utilisateurs})

# Vue pour créer un utilisateur
@transaction.atomic
def creer_utilisateur(request):
    if not request.user.is_authenticated:
        return redirect('page_accueil')

    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    utilisateur = form.save(commit=False)
                    user = User.objects.create_user(username=form.cleaned_data['username'],
                                                    email=form.cleaned_data['email'])
                    user.set_password(form.cleaned_data['password'])
                    user.save()
                    utilisateur.user = user
                    utilisateur.save()
                    utilisateur.bases_de_donnees.set(form.cleaned_data['bases_de_donnees'])
                    messages.success(request, 'Utilisateur créé avec succès.')
            except Exception as e:
                messages.error(request, "Erreur lors de la création de l'utilisateur.")
                transaction.set_rollback(True)

            return redirect('liste_utilisateurs')
        else :
            messages.error(request, "Erreur lors de la création de l'utilisateur.")
    else:
        messages.info(request, 'Veuillez saisir tous les champs.')
        form = UtilisateurCreationForm()

    return render(request, 'creer_utilisateur.html', {'form': form})

# Vue pour modifier un utilisateur
def modifier_utilisateur(request, username):
    if not request.user.is_authenticated:
        return redirect('page_accueil')
    #Search the User and Utilisateur objects by username
    user = User.objects.filter(username=username).first()
    util = Utilisateur.objects.filter(username=username).first()
    if (not user or not util):
        messages.error(request, 'Utilisateur non trouvé!')
        return redirect('liste_utilisateurs')
    utilisateur = get_object_or_404(Utilisateur, username=username)
    if request.method == 'POST':
        form = UtilisateurModificationForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Utilisateur modifié avec succès.')
            return redirect('liste_utilisateurs')
        else :
            messages.error(request, "Erreur dans la modification de l'Utilisateur.")
    else:
        messages.info(request, "Veuillez saisir tous les champs.")
        form = UtilisateurModificationForm(instance=utilisateur)
    return render(request, 'modifier_utilisateur.html', {'form': form})

# Vue pour supprimer un utilisateur
def supprimer_utilisateur(request, username):
    if not request.user.is_authenticated:
        return redirect('page_accueil')
    utilisateur = get_object_or_404(Utilisateur, username=username)
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        user.delete()
        utilisateur.delete()
        messages.success(request, 'Utilisateur supprimé avec succès.')
        return redirect('liste_utilisateurs')
    return render(request, 'supprimer_utilisateur.html', {'utilisateur': utilisateur})

#Se déconnecter
def logout_user(request):
    logout(request)
    return redirect('page_accueil')
