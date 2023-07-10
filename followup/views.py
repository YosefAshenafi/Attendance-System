from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render

from .models import Member
from .forms import LoginForm


def login(request):
    if request.user.is_authenticated:
        return render(request, 'followup/members.html')

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        context = {"forms": form}
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user:
                return render(request, 'followup/members.html', context)
        
        messages.error(request, f'Invalid username or password')
        return render(request, 'followup/login.html', context)
    
    else:
        form = LoginForm()
        context = {"forms": form}
        return render(request, 'followup/login.html', context)
        
        