from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Game, Hand, Score
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, Http404
import uuid

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

    context = {'choice': choice, 'game':game}
    return render(request, 'game.html', context)

@login_required(login_url='/accounts/login')
def join(request, gameid):
    try:
        gameId = uuid.UUID(gameid)
        game = Game.objects.get(game_id=gameId, active=True, is_open=True)
        # Double check there isn't already hand and score models for current player
        hand = Hand.objects.get_or_create(game=game, player=request.user)
        #hand.save()
        score = Score.objects.get_or_create(game=game, player=request.user)
        #score.save()
    except Game.DoesNotExist:
        raise Http404("Given game not found...")

    context = {'choice': 'join', 'game':game, 'hand':hand, 'score':score}
    return render(request, "game.html", context)


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
