from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def login(request):
    if request.method=='POST':
        #username = request.POST['username']
        #password = request.POST['password']

        #user = auth.authenticate(username=username, password=password)

        #if user is not None:
            print('Login successful!')
        #    auth.login(request, user)
            return render(request,'clientmanager.html') # funciona
        #else:
        #    print('User or password not valid!')
        #    #return redirect('login.html')
    else:
        print('render login.html!')
        return render(request,'login.html')     # funciona
        #return redirect('/')