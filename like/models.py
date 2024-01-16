from django.db import models
from django.db.models import ForeignKey


class Like(models.Model):
    post = ForeignKey('Post', related_name='likes', on_delete=models.CASCADE)