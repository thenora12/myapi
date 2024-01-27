# models.py

from django.db import models

class Order(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    date_entree = models.DateField()
    date_livraison = models.DateField()
    note_livreur = models.IntegerField()
    note_gestionnaire = models.IntegerField()
    nom_client = models.CharField(max_length=100)
    tel_client = models.CharField(max_length=15)
    region = models.CharField(max_length=50)
    adresse = models.TextField()
    nom_produit = models.CharField(max_length=100)
    unite = models.CharField(max_length=20)
    prix_propose = models.DecimalField(max_digits=10, decimal_places=2)
    frais_livraison = models.DecimalField(max_digits=10, decimal_places=2)
    gains = models.DecimalField(max_digits=10, decimal_places=2)
    etat_livraison = models.CharField(max_length=20)
    soldee = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    url_order = models.URLField()

    def __str__(self):
        return f"Commande {self.id}"
