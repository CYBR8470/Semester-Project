from django.test import TestCase
from .models import Game, Score, Hand
from django.contrib.auth.models import User

class GameModelTestCase(TestCase):
    """
    Testing the Game Model
    """
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username="testing", email="testing123@abc.com")
        Game.objects.create(host=user, active=True, is_public=True)

    # Testing default values when object is created
    def test_game_defaults_method(self):
        game = Game.objects.get(id=1)
        self.assertTrue(game.active)
        self.assertTrue(game.is_open)
        self.assertTrue(game.is_public)
        self.assertIsNotNone(game.game_id)
        self.assertNotEqual(game.game_id, game.join_code)

class HandModelTestCase(TestCase):
    """
    Testing the Hand Model.
    """
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(id=1, username="testing", email="testing123@abc.com")
        game = Game.objects.create(host=user, active=True, is_public=True)
        Hand.objects.create(game=game, player=user)

    # Testing default values when object is created
    def test_hand_defaults_method(self):
        user = User.objects.get(id=1)
        game = Game.objects.get(id=1)
        hand = Hand.objects.get(id=1)
        self.assertEqual(game.game_id, hand.game.game_id)
        self.assertEqual(user.id, hand.player.id)
        self.assertGreater(hand.d1, 0)
        self.assertGreater(hand.d2, 0)
        self.assertGreater(hand.d3, 0)
        self.assertGreater(hand.d4, 0)
        self.assertGreater(hand.d5, 0)
        self.assertEqual(2, hand.roll_count)
        self.assertEqual(13, hand.rem_rounds)
        self.assertIsNone(hand.yahtzee_flag)

    # Testing roll_count reduction
    def test_hand_reduceRC_method(self):
        hand = Hand.objects.get(id=1)
        self.assertEqual(2, hand.roll_count)
        hand.reduceRC()
        self.assertEqual(1, hand.roll_count)
        hand.reduceRC()
        self.assertEqual(0, hand.roll_count)

    # Testing sumOnes
    def test_hand_sumOnes_method(self):
        hand = Hand.objects.get(id=1)
        # Manually setting dice values so that we can test the sumOnes method
        hand.d1 = 1
        hand.d2 = 3
        hand.d3 = 1
        hand.d4 = 1
        hand.d5 = 5
        sum = hand.sumOnes()
        self.assertEqual(3, sum)
