from rest_framework import serializers
from .models import Comment
from django.contrib.auth import get_user_model


User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','post','content','author','is_from_logged_in_user', 'created', 'updated']