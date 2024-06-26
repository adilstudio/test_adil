"""test_adil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from management import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.page_accueil, name='page_accueil'),
    path('liste-utilisateurs/', views.liste_utilisateurs, name='liste_utilisateurs'),
    path('creer-utilisateur/', views.creer_utilisateur, name='creer_utilisateur'),
    path('modifier-utilisateur/<str:username>/', views.modifier_utilisateur, name='modifier_utilisateur'),
    path('supprimer-utilisateur/<str:username>/', views.supprimer_utilisateur, name='supprimer_utilisateur'),
    path('logout/', views.logout_user, name='logout_user'),
]
