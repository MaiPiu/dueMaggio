# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from gestione.models import *
import datetime

def home (request):
    return render(request,'home.html')
    
def PizzaAll (request):
    listaPiz = Pizza.objects.all()
    var = {'title':'Tutte le Pizze', 'text':'Elenco di tutte le Pizze Disponibili:'}
    
    return render(request,'elenco.htm',{'lista':listaPiz, 'section':var})