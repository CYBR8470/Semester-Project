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
        try:
            hosted_game = Game.objects.get(host=request.user, active=True)
        except Game.DoesNotExist:
            hosted_game = Game(host=request.user, active=True, is_public=True)
            hosted_game.save()            
        finally:
            game = hosted_game

    context = {'choice': choice, 'game':game.game_id}
    return render(request, 'game.html', context)

@login_required(login_url='/accounts/login')
def endgame(request):
    try:
        game_to_end = Game.objects.get(host=request.user, active=True)
        game_to_end.is_open = False
        game_to_end.active = False
        game_to_end.save()
    except Game.DoesNotExist:
        return redirect('index')
    return render(request, 'index.html')

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
