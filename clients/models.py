from django.db import models

# Create your models here.
class Achat(models.Model):
    produit=models.CharField(max_length=255)
    prix=models.IntegerField()
    def __str__(self):
        return self.produit
    
class Client(models.Model):
    
    client=models.CharField(max_length=255)
    achats= models.ManyToManyField(Achat,related_name='liste_achats',blank=True)
    def __str__(self):
        return self.client
    