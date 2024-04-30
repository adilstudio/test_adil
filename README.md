# Gestion des utilisateur


Exercice sur le frameword Django


## Installation

Pour installer l'application il faut tout d'abord cloner le projet sur votre machine en utilisant la commande suivante:

```bash
git clone
```
Puis installer les dépendances en utilisant la commande suivante:

```bash
pip install -r requirements.txt
```

## Afin de lancer le serveur il faut utiliser la commande suivante:

```bash
python manage.py runserver
```

## Pour accéder à l'interface d'administration il faut créer un super utilisateur en utilisant la commande suivante:

```bash
python manage.py createsuperuser
```

## La base de donnée est par défaut en sqlite3.

## On peut utiliser à la place une base de données PostgreSQL, pour ce faire il faut commenter la configuration de la base de données sqlite3 dans le fichier settings.py et décommenter la configuration de la base de données PostgreSQL.

## Puis lancer l'application avec un  un docker compose en utilisant la commande suivante:

```bash
docker-compose up
```

## Mais avant il faudra créer un fichier .env à la racine du projet et ajouter les variables suivantes:

```bash
POSTGRES_USER=root
POSTGRES_PASSWORD=root
```

vous pouvez changer root par les credentials que vous souhaitez.


### Concernant le champ de multiple choix "Basededonnes", nous devrons injecter dans la base les 4 valeurs : Scopus, PubMed, Dimensions et Web of Science

### Pour ce faire, il faut SOIT le faire à travers le shell:

```bash
python manage.py shell
```

### En ajoutant par la commande suivante:

```bash
from gestion_utilisateurs.models import Basededonnes
Basededonnes.objects.create(nom="Scopus")
Basededonnes.objects.create(nom="PubMed")
Basededonnes.objects.create(nom="Dimensions")
Basededonnes.objects.create(nom="Web of Science")
```

### Soit rajouter via l'interface d'administration. Pour pouvoir y accéder, il faut tout d'abord créer un super utilisateur en utilisant la commande suivante:

```bash
python manage.py createsuperuser
```

### Saisir les nouveaux identifiants et se connecter à l'administration sur http://localhost:8000/admin

### Selectionner le model "Basededonnes" et ajouter les 4 valeurs : Scopus, PubMed, Dimensions et Web of Science

### Ainsi, vous pourrez dorénavent créer des utilisateurs avec ces valeurs pour le champ "Basededonnes"



## Pour les tests, il suffit de lancer la commande suivante:

```bash

python manage.py test

```
