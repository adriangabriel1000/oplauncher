from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
                #return render(request, 'user/login.html')
                #return HttpResponse("User authenticated and logged in")
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = LoginForm()

    return render(request, 'user/login.html',{
        'form' : form
    })

def user_logout(request):
    logout(request)
    return redirect('/user/login/')
    #return render(request, 'user/logout.html')
    #return HttpResponse("Logout successful")



def index(request):
    return render(request, 'user/index.html')