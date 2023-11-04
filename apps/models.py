from django.db import models
# Create your models here.
class Contact(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    telephone = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    