from django import forms
from django.forms import ModelForm, Form
from .models import *
 
class MessageForm(forms.ModelForm):
    msg = forms.CharField(required = True, label='', widget = forms.Textarea(attrs= { "rows":4, "cols":50, "placeholder":'Ecris ici une remarque ou message que tu veux partager' })  )

    class Meta :
        model = Message
        fields =  ['msg']
        
STATUS_CHOICES = (
        ('a', 'A faire'),
        ('e', 'En cours'),
        ('t', 'Terminée'),
        ('z', 'Autre'))
class TacheForm(forms.ModelForm):
    titre = forms.CharField(required = True, max_length = 80, widget = forms.Textarea(attrs= { "rows":2, "cols":50, "placeholder":'titre'})  )
    description = forms.CharField(required = False, widget = forms.Textarea(attrs= { "rows":2, "cols":50, "placeholder":'titre'})  )
    deadline = forms.DateField(required = False)
    urgent = forms.BooleanField(required = False)
    pris = forms.BooleanField(required = False)
    pris_par =  forms.CharField(required = False, max_length = 80, widget = forms.Textarea(attrs= { "rows":2, "cols":50, "placeholder":'pris par'})  )
    status = forms.CharField(required = False)
    class Meta :
        model = Tache
        fields =  ['titre', 'description','deadline', 'pris','urgent', 'pris_par', 'status']

class RechercheForm(forms.ModelForm):
    recherche = forms.CharField(required = True, max_length = 80, widget = forms.Textarea(attrs= { "rows":2, "cols":50, "placeholder":'Faire une recherche de tache'})  )
    class Meta :
        model = Recherche
        fields = ['recherche']