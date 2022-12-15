import ctypes
from django.shortcuts import render
from .forms import FormUser
from .forms import FormConnexion
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse
from CV.models import formation,Type
from django.template import loader

def list_form(request):
    form=formation.objects.all().values
    type=Type.objects.all().values
    template=loader.get_template('formation1.html')
    context={
        'form':form,
        'type':type
    }
    return HttpResponse(template.render(context,request))

def del_form(request,id):
    form=formation.objects.get(id=id)
    form.delete()
    return HttpResponseRedirect(reverse('list_form'))

def update_form(request, id):
    form = formation.objects.get(id=id)
    type = Type.objects.all().values()
    template = loader.get_template('updateForm.html')
    context = {
    'form': form,
    'type':type, }
    return HttpResponse(template.render(context, request))

def update_form_action(request,id):
    spe = request.POST['speci']
    l = request.POST['lieu']
    d = request.POST['date']
    t = request.POST['type']
    type = Type.objects.get(id=t)
    form = formation.objects.get(id=id)
    form.speci = spe
    form.lieu = l
    form.date = d
    form.type = type
    form.save()
    return HttpResponseRedirect(reverse('list_form'))
def add_form(request):
    type = Type.objects.all().values()
    template = loader.get_template('addFormation.html')
    context = {
    'type': type,
    }
    return HttpResponse(template.render(context, request))

def add_form_action(request):
    spec = request.POST['speci']
    l = request.POST['lieu']
    d = request.POST['date']
    t = request.POST['type']
    type = Type.objects.get(id=t)
    form = formation(speci=spec, lieu=l, date=d,type=type)
    form.save()
    return HttpResponseRedirect(reverse('list_form'))
def list_type(request):
    type=Type.objects.all().values
    template=loader.get_template('type.html')
    context={
        'type':type,
    }
    return HttpResponse(template.render(context,request))
def del_type(request,id):
    type=Type.objects.get(id=id)
    type.delete()
    return HttpResponseRedirect(reverse('list_type'))
def update_type(request, id):
    type = Type.objects.get(id=id)
    template = loader.get_template('updateType.html')
    context = {

    'type':type, }
    return HttpResponse(template.render(context, request))

def update_type_action(request,id):
    nom = request.POST['type']
    type = Type.objects.get(id=id)
    type.nomType = nom
    type.save()
    return HttpResponseRedirect(reverse('list_type'))
def add_type(request):
    template = loader.get_template('addType.html')
    context = {
    
    }
    return HttpResponse(template.render(context, request))

def add_type_action(request):
    nom = request.POST['type']
    type = Type(nomType=nom)
    type.save()
    return HttpResponseRedirect(reverse('list_type'))

def connect (request):
    connect_form = FormConnexion ()
    return render(request, 'connexion.html', {'connect_form' : connect_form }) 

def signIn(request):
    username = request.POST['login']
    password = request.POST['mot2pass']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        request.session['username'] = username 
        return HttpResponseRedirect(reverse('list_form'))
    
    else:
        ctypes.windll.user32.MessageBoxW(0, "Login et/ou mot de passe incorrect", "Erreur", 1)
        return HttpResponseRedirect(reverse('connect'))
def signOut(request):
    logout(request) 
    return HttpResponseRedirect(reverse('connect'))