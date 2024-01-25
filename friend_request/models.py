from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import OneToOneField, ForeignKey

User = get_user_model()


class FriendRequest(models.Model):
    PENDING = 0
    ACCEPTED = 1
    REJECTED = 2

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected')
    ]

    status = models.IntegerField(choices=STATUS_CHOICES, default=PENDING)
    requester = ForeignKey(User, related_name="requester_user", on_delete=models.CASCADE)
    receiver = ForeignKey(User, related_name="receiver_user", on_delete=models.CASCADE)