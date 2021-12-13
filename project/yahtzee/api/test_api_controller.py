from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from yahtzee.frontend.models import Game, Score, Hand
from django.contrib.auth.models import User

class GameListTestCase(APITestCase):
    """
        Basic Unit Tests for the GameList API endpoints
    """
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username="testing", email="testing123@abc.com")
        game = Game.objects.create(host=user, active=True, is_public=True)
        Hand.objects.create(player=user,game=game)
        Score.objects.create(player=user,game=game)

    # Make sure get method returns successfully
    def test_gamelist_get(self):
        game = Game.objects.get(id=1)
        response = self.client.get(reverse("games"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(str(response.data[0]['username']), 'testing')
        self.assertEqual(str(response.data[0]['game_id']), str(game.game_id))