from django.urls import path
from . import views


urlpatterns = [ path('', views.index, name ='index'),
path('chants', views.chants, name ='chants'),
path('equipe', views.equipe, name ='equipe'),
path('evenements', views.evenements, name ='evenements'),
path('partenaires', views.partenaires, name ='partenaires'),
#path('membres/', views.membre_msg.as_view(), name='membre_msg'),
path('form/', views.message_form, name='form'),
#path('form2/', views.new_msg, name='form2'),
path('tache/<int:id>/', views.tache, name='tache'),
path('new_tache/', views.new_tache, name='new_tache'),
path('perso/', views.perso, name='perso'),
path('perso/', views.perso, name='perso'),
path('faq/', views.faq, name='faq'),
path('prendre_tache/<int:id>/', views.prendre_tache, name='prendre_tache'),
path('plus_prendre_tache/<int:id>/', views.plus_prendre_tache, name='plus_prendre_tache'),
path('plus_prendre_tache_perso/<int:id>/', views.plus_prendre_tache_perso, name='plus_prendre_tache_perso'),
path('supprimer_tache/<int:id>/', views.supprime_tache, name='supprime_tache'),
path('supprimer_msg/<int:id>/', views.supprime_msg, name='supprime_msg'),
path('supprimer_tache_perso/<int:id>/', views.supprime_tache_perso, name='supprime_tache_perso'),


]