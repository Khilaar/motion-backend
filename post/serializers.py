from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Post

User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'date_created', 'date_updated', 'author', 'images']
        read_only_fields = ['author']

        def to_representation(self, instance):
            representation = super().to_representation(instance)
            representation['author'] = AuthorSerializer(instance.author).data
            return representation
