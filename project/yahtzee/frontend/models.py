import uuid
from django.db import models
from django.conf import settings

class Game(models.Model):
    game_id = models.UUIDField(default=uuid.uuid4, editable=False)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    is_public = models.BooleanField()
    join_code = models.CharField(max_length=100, null=True)
    active = models.BooleanField(default=True)