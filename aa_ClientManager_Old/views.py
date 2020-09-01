from django.shortcuts import render

from django.http import HttpResponse

from .models import clients, catalog, backlog

# Create your views here.

def home(request):

    catalogs = catalog.objects.all()
    return render(request,'login.html', {'catalogs': catalogs})