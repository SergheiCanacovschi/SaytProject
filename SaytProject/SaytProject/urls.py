
"""WebBooks URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('catalog/', include('catalog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from News import views
from django.conf.urls.static import static
from django.conf import settings
import os


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('passport',views.passport, name='passport'),
    path('simvol',views.simvol, name='simvol'),
    path('prim',views.prim, name='prim'),
    path('decont',views.decont, name='decont'),
    path('covid',views.covid, name='covid'),
    path('decent',views.decent, name='decent'),
    path('pred',views.pred, name='pred'),
    path('secret',views.secret, name='secret'),
    path('sovet',views.sovet, name='sovet'),
    path('contacti',views.contacti, name='contacti'),
    path('speccom',views.speccom, name='speccom'),
    path('rasp',views.rasp, name='rasp'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

   



   
 #   re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='doc-detail'),




