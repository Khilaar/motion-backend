from django.db import models
from django.db.models import ForeignKey


class Like(models.Model):
    post = ForeignKey('post.Post', related_name='likes_post_rel', on_delete=models.CASCADE)