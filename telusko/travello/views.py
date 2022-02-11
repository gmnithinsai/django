from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    

    return render(request, 'index.html', {'dests': dests})

def tirupati(request):
    return render(request, 'tirupati.html')

def hyderabad(request):
    return render(request, 'hyderabad.html')

def mumbai(request):
    return render(request, 'mumbai.html')

def bangalore(request):
    return render(request, 'bangalore.html')

