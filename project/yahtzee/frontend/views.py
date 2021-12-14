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
def action(request, gameid, action):
    game = Game.objects.get(game_id=gameid)
    hand = Hand.objects.get(game=game, player=request.user)
    score = Score.objects.get(game=game, player=request.user)

    if (action == 'setOnes'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.ones is None):
            #Then the calculated value based on the dice is saved to the score
            score.ones = hand.sumOnes()
            #For Joker rules, we need to check if this is a bonus yahtzee
            if (hand.yahtzee_flag == 1 and hand.yahtzee() == 50 ):
                #If so, we increment the number of bonus_yahtzees
                score.bonus_yahtzees += 1
            score.save()
            #Next we reset the dice and decrease the number of rem_rounds by 1
            hand.roll_count = 2
            hand.rem_rounds -= 1
            hand.init()
            #Because hand.init() saves we do not need to do so here
    if (action == 'setFives'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.fives is None):
            #Then the calculated value based on the dice is saved to the score
            score.fives = hand.sumFives()
            #For Joker rules, we need to check if this is a bonus yahtzee
            if (hand.yahtzee_flag == 1 and hand.yahtzee() == 50 ):
                #If so, we increment the number of bonus_yahtzees
                score.bonus_yahtzees += 1
            score.save()
            #Next we reset the dice and decrease the number of rem_rounds by 1
            hand.roll_count = 2
            hand.rem_rounds -= 1
            hand.init()
            #Because hand.init() saves we do not need to do so here

    if (action == 'setYahtzee'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.yahtzee is None):
            #Then the calculated value based on the dice is saved to the score
            score.yahtzee = hand.yahtzee()
            score.save()
            #For Joker rules, we need to set the yahtzee flag to 0 or 1
            if ( hand.yahtzee() == 50 ):
                hand.yahtzee_flag = 1
            else:
                hand.yahtzee_flag = 0
            #Next we reset the dice and decrease the number of rem_rounds by 1
            hand.roll_count = 2
            hand.rem_rounds -= 1
            hand.init()

    if (action == 'setTwos'):
        if (score.twos is None):
            score.twos = hand.sumTwos()
            score.save()
            game.rem_rounds -= 1
            game.save()
            print("setTwos called")

    if (action == 'setThrees'):
        if (score.threes is None):
            score.threes = hand.sumThrees()
            score.save()
            game.rem_rounds -= 1
            game.save()
            print("setThrees called")

    if (action == 'setFours'):
        if (score.fours is None):
            score.fours = hand.sumFours()
            score.save()
            game.rem_rounds -= 1
            game.save()
            print("setFours called")

    if (action == 'setFives'):
        if (score.fives is None):
            score.fives = hand.sumFives()
            score.save()
            game.rem_rounds -= 1
            game.save()
            print("setFives called")

    if (action == 'setSixes'):
        if (score.sixes is None):
            score.sixes = hand.sumSixes()
            score.save()
            game.rem_rounds -= 1
            game.save()
            print("setSixes called")

    context = {'game':game, 'hand':hand, 'score':score}
    return render(request, 'game.html', context)

@login_required(login_url='/accounts/login')
def board(request, gameid):
    game = Game.objects.get(game_id=gameid)
    hand = Hand.objects.get(game=game, player=request.user)
    score = Score.objects.get(game=game, player=request.user)
    context = {'game':game, 'hand':hand, 'score':score}
    return render(request, 'board.html', context)

@login_required(login_url='/accounts/login')
def gameSetup(request, choice):
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
        return render(request, "game.html", context)

@login_required(login_url='/accounts/login')
def join(request, gameid):
    try:
        gameId = uuid.UUID(gameid)
        game = Game.objects.get(game_id=gameId, active=True, is_open=True)
        # Double check there isn't already hand and score models for current player
        hand = Hand.objects.get_or_create(game=game, player=request.user)
        score = Score.objects.get_or_create(game=game, player=request.user)
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
