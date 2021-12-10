from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Game, Hand, Score
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
        # Pull associated hand
        try:
            player_hand = Hand.objects.get(game=hosted_game, player=request.user)
        except Hand.DoesNotExist:
            player_hand = Hand(game=hosted_game, player=request.user)
            player_hand.save()
        finally:
            hand = player_hand
        # Pull associated scoreboard
        try:
            player_score = Score.objects.get(game=hosted_game, player=request.user)
        except Score.DoesNotExist:
            player_score = Score(game=hosted_game, player=request.user)
            player_score.save()
        finally:
            score = player_score

    context = {'choice': choice, 'game':game, 'hand':hand, 'score':score}
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
