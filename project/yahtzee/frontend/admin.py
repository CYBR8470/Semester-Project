from django.contrib import admin
from .models import Game, Hand, Score

# Register your models here.
admin.site.register(Game)
admin.site.register(Hand)
admin.site.register(Score)
