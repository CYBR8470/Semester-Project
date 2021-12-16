from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from yahtzee.api.serializers import GameSerializer, HandSerializer
from yahtzee.frontend.models import Game, Hand
import uuid

class GameList(APIView):
    """
        List all active games
    """
    def get(self, request, format=None):
        games = Game.objects.filter(active__exact=True)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

class  GameDetail(APIView):
    """
        Retrieve, update or delete a Game instance
    """
    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, gameid, format=None):
        gameId = uuid.UUID(gameid)
        is_game_admin = request.user.groups.filter(name='game_admin').exists()
        if is_game_admin == False:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            game = Game.objects.get(game_id=gameId)
        except Game.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BoardRollDice(APIView):
    """
        Sets new dice values, saves hand and returns values.
    """
    def post(self, request):
        data = request.data
        gameId = uuid.UUID(data['game'])
        game = Game.objects.get(game_id=gameId)
        player = int(data['player'])
        try:
            hand = Hand.objects.get(game=game, player=player)
        except Hand.DoesNotExist:
            hand = Hand(game=game, player=player)
            hand.save()
        hand.d1 = hand.rolldice(int(data['d1']))
        hand.d2 = hand.rolldice(int(data['d2']))
        hand.d3 = hand.rolldice(int(data['d3']))
        hand.d4 = hand.rolldice(int(data['d4']))
        hand.d5 = hand.rolldice(int(data['d5']))
        hand.reduceRC()
        hand.save()
        serializer = HandSerializer(hand)
        return Response(serializer.data)
        
        




