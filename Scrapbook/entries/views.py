from django.shortcuts import render, HttpResponse
from .models import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def entry(request):
    names = ['Mom', 'Dad','Kartikee','Jetal','Aai','Chirag','CJ','Shreyas','Amol','Manasi','Urmi','Kush','Vidhita','Rosita','Sarthak','Lokita','Mangu','Kiki','Prateek','Atman','KC','Yash','KJ']
    name = ''
    msg = ''
    obj = None
    if request.method == "POST":
        for name in names:
            if name in request.POST:
                obj = Person.objects.get(name=name)
    context = {'obj': obj}
    return render(request, 'entry.html', context)

def close(request):
    return render(request, 'close.html')

def wall(request):
    return render(request, 'wall.html')

def family(request):
    return render(request, 'family.html')

def scar(request):
    return render(request, 'scar.html')

def fomo(request):
    return render(request, 'fomo.html')

def dates(request):
    return render(request, 'dates.html')