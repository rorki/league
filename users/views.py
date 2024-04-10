from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import auth

def login(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(request, username=username, password=password)
            
            if user:
                auth.login(request, user)
                return redirect('league')
    else:
        form = LoginForm()
   
    return render(request, 'login.html', {'form': form})

def logout(request):
    
    auth.logout(request)
    return redirect('login')