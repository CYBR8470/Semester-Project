from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Game
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
    if(choice == 'host'):
        # Need to check for active games attached to this user.
        hosted_game = Game.objects.all().filter(host=request.user).filter(active=True)[0]
        # if game doesn't exist, create new game
        if not hosted_game:
            hosted_game = Game.objects.create(host=request.user, is_public = True)
            hosted_game.save()
        game = hosted_game
        


    context = {'choice': choice, 'game':game}
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
