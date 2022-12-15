from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from CV.models import competance,stage,formation

def index(request):
    template=loader.get_template('infosGenerales.html')
    context={
        'description':'Malek Ayed étudiante en 2ème année dans le domaine de technologie de l`informatique à Iset Nabeul , spécialité développement des systémes d`information passionné par le Tennis',
        'mail':'malek25ayed@gmail.com',
        'telephone':'29*****',
        'adresse': 'rue Grand Maghreb ,Dar Chaben El Fehri ,Nabeul '  ,
        'datedenaissance':'25 Mars 2002'  
    }
    return HttpResponse(template.render(context,request))
def list_comp(request):    
    comp=competance.objects.all().values
    template=loader.get_template('competances.html')
    context={
        'comp':comp,
    }
    return HttpResponse(template.render(context,request))
def list_stage(request):
    stg=stage.objects.all().values
    template=loader.get_template('stage.html')
    context={
        'stg':stg,
    }    
    return HttpResponse(template.render(context,request))
def list_formation(request):
    form=formation.objects.all().values
    template=loader.get_template('formation.html')
    context={
        'form':form
    }
    return HttpResponse(template.render(context,request))



   


