# Generated by Django 4.2.11 on 2024-05-01 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("management", "0002_alter_basededonnees_nom"),
    ]

    operations = [
        migrations.RenameField(
            model_name="utilisateur",
            old_name="adresse_email",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="utilisateur",
            old_name="mot_de_passe",
            new_name="first_name",
        ),
        migrations.RenameField(
            model_name="utilisateur",
            old_name="nom",
            new_name="last_name",
        ),
        migrations.RenameField(
            model_name="utilisateur",
            old_name="prenom",
            new_name="password",
        ),
        migrations.AddField(
            model_name="utilisateur",
            name="user",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
