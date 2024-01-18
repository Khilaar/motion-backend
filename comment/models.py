from django.contrib.auth import get_user_model
from django.db import models



User = get_user_model()

class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='post_to_user', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='comment_user_rel', on_delete=models.CASCADE)
    is_from_logged_in_user = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
