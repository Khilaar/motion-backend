from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import ManyToManyField, ForeignKey

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    images = models.ImageField(upload_to='')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    original_post = models.ForeignKey('Post', related_name='original_post_shared_post_rel', blank=True, on_delete=models.CASCADE)
