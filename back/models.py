from django.db import models

# Create your models here.

class User(models.Model):
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50,  blank=True)
    poste = models.CharField(max_length=50,  blank=True, null = True)

    def __str__(self):
        """String for representing the Model object."""
        return self.prenom

class Tache(models.Model):
    titre = models.CharField(max_length=120)
    description =  models.TextField( blank=True, null = True) 
    deadline = models.DateField( blank=True, null = True)
    pris = models.BooleanField(null = True, blank = True)
    fait_par = models.CharField(max_length=50, blank=True)
    urgent = models.BooleanField(blank = True)
    pris_par = models.CharField(max_length=50, blank=True, null = True)
    choix_pris_par = models.ManyToManyField(User, blank = True, null = True)
    def __str__(self):
        """String for representing the Model object."""
        return self.titre
    def get_absolute_url(self):
        return f"/back/tache/{self.id}"


    LOAN_STATUS = (
        ('a', 'A faire'),
        ('e', 'En cours'),
        ('t', 'Terminée'),
        ('z', 'Autre'))
    status = models.CharField(max_length=50, blank=True, help_text ="Choisir l'état d'avancement de la tâche" ,default = 'à faire')

    class Meta:
        ordering = ['deadline']

class Message(models.Model):
    msg = models.TextField( blank=True) 
    prenom = models.CharField(max_length=50, null=True, blank = False)
    date = models.DateTimeField( auto_now=True)

    class Meta:
        ordering = ['-date']


