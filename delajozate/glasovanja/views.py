# Create your views here.

import datetime

from django.shortcuts import render
from django.http import Http404

from magnetogrami.models import Glasovanje, Glas

def index(request):
    context = {
        'object_list': Glasovanje.objects.all().select_related('seja'),
        }
    return render(request, 'glasovanja.html', context)

def glasovanje(request, datum, ura=None, pk=None):
    datum = datetime.datetime.strptime(datum, '%Y-%m-%d').date()
    
    if ura is not None:
        ura = datetime.datetime.strptime(ura, '%H:%M:%S').time()
        glasovi = Glas.objects.filter(
            glasovanje__datum=datum,
            glasovanje__ura=ura)
    elif pk is not None:
        glasovi.filter(glasovanje__id=pk)
    else:
        raise Http404
    
    glasovi = glasovi.select_related('oseba')
    context = {
        'objects': glasovi
    }
    return render(request, 'glasovanje.html', context)