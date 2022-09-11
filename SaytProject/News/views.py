from email.mime import image
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
   
    summary = Novosti.objects.order_by('-id')
    return render(request,"index.html", context={'summary': summary,
   
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
def decont(request):

    return render(request,"./pages/decont.html",context={
    }
    )  

def covid(request):

    return render(request,"./pages/covid.html",context={
    }
    )  
def pred(request):

    return render(request,"./pages/pred.html",context={
    }
    ) 
def decent(request):

    return render(request,"./pages/decent.html",context={
    }
    ) 
def secret(request):

    return render(request,"./pages/secret.html",context={
    }
    ) 
def sovet(request):

    return render(request,"./pages/sovet.html",context={
    }
    ) 
def contacti(request):

    return render(request,"./pages/contacti.html",context={
    }
    ) 
def speccom(request):

    return render(request,"./pages/speccom.html",context={
    }
    )
def rasp(request):
    title = Rasporejenia.objects.order_by('-id')
    return render(request,"./pages/rasp.html", context={'title': title,
   
    }
                 )

def ruc(request):

    return render(request,"./pages/ruc.html",context={
    }
    )

def apar(request):

    return render(request,"./pages/apar.html",context={
    }
    )

def resh(request):
    title = KCS.objects.order_by('-id')
    return render(request,"./pages/resh.html",context={
    }
    )
 
