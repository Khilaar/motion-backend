from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import FriendRequest
from django.shortcuts import get_object_or_404

User = get_user_model()

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'status', 'requester', 'receiver']

    def create(self, validated_data):
        requester = self.context['request'].user
        receiver_id = self.context['view'].kwargs['pk']
        status = FriendRequest.PENDING

        receiver = get_object_or_404(User, id=receiver_id)

        friend_request = FriendRequest.objects.create(
            requester=requester,
            receiver=receiver,
            status=status
        )

        return friend_request