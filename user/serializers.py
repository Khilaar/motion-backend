from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    user_following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'avatar', 'job', 'banner', 'location', 'phone_number', 'about_me', 'things_user_likes', 'comments', 'user_following']

    def get_user_following(self, obj):
        following_users = obj.user_following.all()
        return UserSerializer(following_users, many=True).data