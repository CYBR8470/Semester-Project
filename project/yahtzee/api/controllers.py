from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from django.shortcuts import render
from django.db import models
from yahtzee.api.serializers import GameSerializer
from yahtzee.frontend.models import Game

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
    
    def delete(self, request, pk, format=None):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



