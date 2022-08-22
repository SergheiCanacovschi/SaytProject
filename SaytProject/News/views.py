from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return ("Главная страница сайта Районный Совет")

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views import generic


# Create your views here.

def index(request):
    num_document = Document.objects.all().count()
    num_novosti = Novosti.objects.all().count()
    return render(request,"index.html",context={
    'num_document':num_document,
    'num_novosti':num_novosti,
    }
                 )

def passport(request):

    return render(request,"./pages/passport.html",context={
    }
    )
def simvol(request):

    return render(request,"./pages/simvol.html",context={
    }
    )
def prim(request):

    return render(request,"./pages/prim.html",context={
    }
    )
   