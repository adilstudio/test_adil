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

## On peut utiliser à la place une base de données PostgreSQL, pour ce faire il faut lancer l'application avec un  un docker compose en utilisant la commande suivante:

```bash
docker-compose up
```

## Mais avant il faudra créer un fichier .env à la racine du projet et ajouter les variables suivantes:

```bash
POSTGRES_USER=root
POSTGRES_PASSWORD=root
```

vous pouvez changer root par les credentials que vous souhaitez.
