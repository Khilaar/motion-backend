from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import OneToOneField


class User(AbstractUser):
    avatar = models.ImageField(upload_to='', blank=True, null=True)
    comments = models.ForeignKey(to='comment.Comment', related_name="user_comments", on_delete=models.CASCADE, blank=True, null=True)
    job = models.CharField(max_length=200, blank=True)
    banner = models.ImageField(upload_to='', blank=True)
    location = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)
    about_me = models.TextField(max_length=1000, blank=True)
    things_user_likes = models.TextField(max_length=500, blank=True)
    custom_users_following = models.ManyToManyField(to='User', related_name="custom_users_follower", blank=True)
    friend_request = OneToOneField(to="friend_request.FriendRequest", related_name="users_friend_request", on_delete=models.CASCADE, blank=True, null=True)
    friend_request_receiver = OneToOneField(to="friend_request.FriendRequest", related_name="users_friend_request_receiver", on_delete=models.CASCADE, blank=True, null=True)

