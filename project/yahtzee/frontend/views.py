from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    is_authenticated = request.user.is_authenticated
    context = {'authenticated': is_authenticated}
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login')
def game(request, choice):
    context = {'choice': choice}
    return render(request, 'game.html', context)

def loginUser(request):
    return render(request, 'login.html')

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect('index')

        messages.error(request, "Unsuccessful registration. Invalid Information.")
    form=NewUserForm
    return render(request, 'register.html')
