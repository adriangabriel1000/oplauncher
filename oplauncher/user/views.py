from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistraionForm
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

def accSettings(request):
    return render(request, 'user/account_settings.html')

def register(request):
    if request.method == 'POST':
        user_form = UserRegistraionForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return render(request, '')
    else:
        user_form = UserRegistrationForm()
    return render(request, '', {
        'user_form': user_form
    })

def index(request):
    return render(request, 'user/index.html')