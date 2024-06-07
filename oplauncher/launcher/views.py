from django.shortcuts import render
from .models import Quals

# Create your views here.

def index(request):
    quals = Quals.objects.all()
    return render(request, 'launcher/index.html', {
        'quals': quals,
        
    })
