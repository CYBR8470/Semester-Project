from django.test import TestCase
from .models import Game, Score, Hand
from django.urls import reverse
from django.contrib.auth.models import User

class IndexViewTestCase(TestCase):
    """
    Basic unit tests for the index view
    """
    # Make sure we don't get any exceptions trying to load the view
    def test_index_url_exists(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
    
    # Make sure correct template is used when hitting this view method
    def test_index_uses_correct_template(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
