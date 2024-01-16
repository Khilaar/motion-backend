from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to='')
    job = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='')
    posts = models.ForeignKey(to='post.Post', on_delete=models.CASCADE)
    comments = models.ForeignKey(to='comment.Comment', on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    about_me = models.TextField(max_length=1000)
    things_user_likes = models.TextField(max_length=500)
    following = models.ManyToManyField(to='User')
    followers = models.ManyToManyField(to='User')
    friend_request = models.OneToOneField(to='friend_request.FriendRequest', on_delete=models.CASCADE)
    friend_request_receiver = models.OneToOneField(to='friend_request.FriendRequest', on_delete=models.CASCADE)
