from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'job', 'banner', 'location', 'phone_number', 'about_me', 'things_user_likes', 'comments', 'custom_users_following']

