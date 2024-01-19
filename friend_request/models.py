from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import OneToOneField

class FriendRequest(models.Model):
    status = models.IntegerField()
    requester = OneToOneField('user.User', related_name="requester_user", on_delete=models.CASCADE)
    receiver = OneToOneField('user.User', on_delete=models.CASCADE)