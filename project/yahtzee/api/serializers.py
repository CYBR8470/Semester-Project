from rest_framework import serializers
from yahtzee.frontend.models import Game
from django.contrib.auth.models import User

class AuthUserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class GameSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='host.username')
    class Meta:
        model = Game
        fields = ('id', 'game_id', 'is_public', 'join_code', 'host', 'active', 'is_open', 'username')
