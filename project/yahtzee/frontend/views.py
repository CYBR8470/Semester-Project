from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Game, Hand, Score
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, Http404
import uuid
import cgi

def index(request):
    is_authenticated = request.user.is_authenticated
    context = {'authenticated': is_authenticated}
    return render(request, 'index.html', context)

@login_required(login_url='/accounts/login')
def action(request, gameid, action):
    game = Game.objects.get(game_id=gameid)
    hand = Hand.objects.get(game=game, player=request.user)
    score = Score.objects.get(game=game, player=request.user)

    def bonusYahtzee():
        #For Joker rules, we need to check if this is a bonus yahtzee
        if (hand.yahtzee_flag == 1 and hand.yahtzee() == 50 ):
            #If so, we increment the number of bonus_yahtzees
            score.bonus_yahtzees += 1
        score.save()

    if (action == 'setOnes'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.ones is None):
            #Then the calculated value based on the dice is saved to the score
            score.ones = hand.sumOnes()
            bonusYahtzee()
            hand.init()

    if (action == 'setTwos'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.twos is None):
            #Then the calculated value based on the dice is saved to the score
            score.twos = hand.sumTwos()
            bonusYahtzee()
            hand.init()

    if (action == 'setThrees'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.threes is None):
            #Then the calculated value based on the dice is saved to the score
            score.threes = hand.sumThrees()
            bonusYahtzee()
            hand.init()

    if (action == 'setFours'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.fours is None):
            #Then the calculated value based on the dice is saved to the score
            score.fours = hand.sumFours()
            bonusYahtzee()
            hand.init()

    if (action == 'setFives'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.fives is None):
            #Then the calculated value based on the dice is saved to the score
            score.fives = hand.sumFives()
            bonusYahtzee()
            hand.init()

    if (action == 'setSixes'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.sixes is None):
            #Then the calculated value based on the dice is saved to the score
            score.sixes = hand.sumSixes()
            bonusYahtzee()
            hand.init()

    if (action == 'setThreeOAK'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.three_oak is None):
            #Then the calculated value based on the dice is saved to the score
            score.three_oak = hand.threeOAK()
            bonusYahtzee()
            hand.init()

    if (action == 'setFourOAK'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.four_oak is None):
            #Then the calculated value based on the dice is saved to the score
            score.four_oak = hand.fourOAK()
            bonusYahtzee()
            hand.init()

    if (action == 'setFullHouse'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.full_house is None):
            #Then the calculated value based on the dice is saved to the score
            score.full_house = hand.fullHouse()
            bonusYahtzee()
            hand.init()

    if (action == 'setSmallStraight'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.small_straight is None):
            #Then the calculated value based on the dice is saved to the score
            score.small_straight = hand.smallStraight()
            bonusYahtzee()
            hand.init()

    if (action == 'setLargeStraight'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.large_straight is None):
            #Then the calculated value based on the dice is saved to the score
            score.large_straight = hand.largeStraight()
            bonusYahtzee()
            hand.init()

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
            #Finally we reset the dice
            hand.init()

    if (action == 'setChance'):
        #First we check that the field is empty, so that data is not overwritten
        if (score.chance is None):
            #Then the calculated value based on the dice is saved to the score
            score.chance = hand.chance()
            bonusYahtzee()
            hand.init()

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
            game.players.add(hand)
        # Pull associated scoreboard
        try:
            player_score = Score.objects.get(game=hosted_game, player=request.user)
        except Score.DoesNotExist:
            player_score = Score(game=hosted_game, player=request.user)
            player_score.save()
        finally:
            score = player_score
            game.scores.add(score)

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
