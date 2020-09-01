from django.shortcuts import render, redirect
from ClientManager.models import clients
from django.contrib import messages
from django.contrib.auth.models import User, auth
#from .forms import clientRegister

# Create your views here.

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login successful!')
            return redirect('/')
        else:
            print('User or password not valid!')
            return redirect('login.html')
    else:
        print('render login.html!')
        return render(request,'login.html')

def register_client(request):

    if request.method == 'POST':
        name = request.POST['name']
        nif = request.POST['nif']
        mail = request.POST['mail']
        date_birth = request.POST['date_birth']
        user.save()

    else:
        return render(request, 'register_client.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def clientRegister_view(request):
    form = clientRegister(request.POST or None)
    if form.is_valid():
        form.save()

    context={
        'form': form
    }
    return render(request, 'register_client.html', context)