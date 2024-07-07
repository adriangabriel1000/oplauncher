from django.shortcuts import render
from .models import Quals
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def index(request):
    quals = Quals.objects.all()
    
    return render(request, 'launcher/index.html', {
        'quals': quals,
    })

def accSettigns(request):
    return render(request, 'user/account_settings.html')
    