from django.db import models
from django.db.models import OneToOneField


class FriendRequest(models.Model):
    status = models.IntegerField()
    requester = OneToOneField('user.User', on_delete=models.CASCADE)
    receiver = OneToOneField('user.User', on_delete=models.CASCADE)