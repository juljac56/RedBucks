from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from back.models import *
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime 
from django.db.models import Q

from .forms import *

# Create your views here.

def index(request):
    return render(request,'./template/home.html')

def chants(request):
    return render(request,'./template/chants.html')

def equipe(request):
    return render(request,'./template/equipe.html')

def evenements(request):
    return render(request,'./template/evenements.html')

def partenaires(request):
    return render(request,'./template/partenaires.html')

"""
class membre_msg (LoginRequiredMixin, generic.ListView):
    model = Message
    context_object_name = 'msg_list'   # your own name for the list as a template variable
    template_name = './template/page_membre.html'  # Specify your own template name/location

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(membre_msg , self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['en plus'] = 'context en plus test'
        return context
"""
@login_required(redirect_field_name='./templates/registration/login.html')
def message_form(request):
    username = request.user.username
    form_msg = MessageForm(request.POST or None)
    form_recherche = RechercheForm(request.POST or None)
    queryset = Message.objects.all()[:20]
    tache = Tache.objects.all()
    date = datetime.date.today() - datetime.timedelta(days=7)
    liste_tache = Tache.objects.all()
    for l in liste_tache:
        if l.deadline != None:
            if l.deadline < date:
                l.delete()
  
    perso = User.objects.get(prenom = username) #pour afficher les taches prises perso
    id = perso.id
    tache_perso = Tache.objects.filter(choix_pris_par = id)
    if form_recherche.is_valid():
        recherche = form_recherche.save(commit = False)
        test =  recherche.recherche
        tache = Tache.objects.filter( Q(titre__icontains = test)| Q(fait_par= test) )

    if form_msg != None:
        if form_msg.is_valid():
            new = form_msg.save(commit = False)
            new.prenom = username
            new.save()
            return HttpResponseRedirect(request.path_info)
        else:
            print(form_msg.errors)
    context = {
        'form_msg' : form_msg,
        'msg_list' : queryset,
        'tache_list' : tache,
        'tache_perso_list':tache_perso,
        'prenom':username,
        
    }
    return render(request, "./template/form.html", context)

@login_required(redirect_field_name='./templates/registration/login.html')
def test_msg(request):
    form_msg = MessageForm(request.POST or None)
    queryset = Message.objects.all()[:20]
    tache = Tache.objects.all()
    date = datetime.date.today() - datetime.timedelta(days=7)
    liste_tache = Tache.objects.all()

   
    context = {
        'msg_list' : queryset,
        
        
    }
    return render(request, "./template/test_msg.html", context)


@login_required(redirect_field_name='./templates/registration/login.html')
@csrf_exempt
def tache(request, id):
    
    form_tache = TacheForm(request.POST or None)
    
    if form_tache.is_valid():
        perso = Tache.objects.get(id=id).fait_par
        Tache.objects.filter(id=id).delete()
        new = form_tache.save(commit = False)
        new.id = id
        if perso == None:
            new.fait_par = request.user.username
        else:
            new.fait_par = perso
        new.save()
        return redirect('../../form/')
    else:
        print(form_tache.errors)
    obj  = get_object_or_404(Tache,id= id)
    context= {"tache":obj,
    "form_tache": form_tache,
    "status" : ["A faire", "En cours", "Terminée","Autre"]}


    return render(request, "./template/tache.html", context)

@login_required(redirect_field_name='./templates/registration/login.html')
@csrf_exempt
def new_tache(request):
    
    form_tache = TacheForm(request.POST or None)
    
    if form_tache.is_valid():
        new = form_tache.save(commit=False)
        new.fait_par = request.user.username
        new.save()
        return redirect('../form/')
    else:
        print(form_tache.errors)
    context= { "form_tache": form_tache,
    "status" : ["A faire", "En cours", "Terminée","Autre"]}


    return render(request, "./template/new_tache.html", context)

@login_required(redirect_field_name='./templates/registration/login.html')
def prendre_tache(request, id):
        tache = Tache.objects.get(id =id)
        prenom = request.user.username
        perso = User.objects.get(prenom = prenom)
        id = perso.id
        tache.choix_pris_par.add(id)
        return redirect('../../form/')

@login_required(redirect_field_name='./templates/registration/login.html')
def plus_prendre_tache(request, id):
        tache = Tache.objects.get(id =id)
        prenom = request.user.username
        perso = User.objects.get(prenom = prenom)
        id = perso.id
        tache.choix_pris_par.remove(id)

        return redirect('../../form/')
@login_required(redirect_field_name='./templates/registration/login.html')
def plus_prendre_tache_perso(request, id):
        tache = Tache.objects.get(id =id)
        prenom = request.user.username
        perso = User.objects.get(prenom = prenom)
        id = perso.id
        tache.choix_pris_par.remove(id)

        return redirect('../../perso/')

"""
def new_msg(request):
    if request.method =="POST":
        my_form = New_msg(request.POST)
        if my_form.is_valid():
            Message.objects.create(**my_form.cleaned_data)
            return http.HttpResponseRedirect('')
        else:
            print(my_form.errors)

    return render(request, "./template/form2.html")
""" 
@login_required(redirect_field_name='./templates/registration/login.html')
def delete_msg(request, id):
    obj  = get_object_or_404(Product, id = id)
    obj.delete()
    return redirect('../../form/')
    context = {"object": obj}
    return render(request, "products/msg_delete.html", context)

@login_required(redirect_field_name='./templates/registration/login.html')
def supprime_msg(request, id):
    msg = get_object_or_404(Message, id = id)
    msg.delete()
    return redirect('../../form/')


@login_required(redirect_field_name='./templates/registration/login.html')
def supprime_tache(request, id):
    tache = get_object_or_404(Tache, id = id)
    tache.delete()
    return redirect('../../form/')

@login_required(redirect_field_name='./templates/registration/login.html')
def supprime_tache_perso(request, id):
    tache = get_object_or_404(Tache, id = id)
    tache.delete()
    return redirect('../../perso/')

@login_required(redirect_field_name='./templates/registration/login.html')
def perso(request):
    prenom = request.user.username
    perso = User.objects.get(prenom = prenom)
    id = perso.id
    tache = Tache.objects.filter(choix_pris_par = id)
    context = {'tache_list': tache,
    'prenom':prenom,}



    return render(request, "./template/perso.html", context)

@login_required(redirect_field_name='./templates/registration/login.html')

def faq(request):
    return render(request,'./template/faq.html')


"""
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from catalog.models import Author

class AuthorCreate(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    initial = {'date_of_death': '11/06/2020'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)

class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors') """