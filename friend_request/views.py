from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FriendRequest
from .serializers import FriendRequestSerializer
from django.shortcuts import get_object_or_404

User = get_user_model()


# Create your views here.
from rest_framework import status
from rest_framework.response import Response


#When we send a request in the frontend we need to add the requester id and the receiver id in the body. "requester" & "receiver"
class SendFriendRequestView(CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        requester = self.request.user
        receiver_id = self.kwargs['pk']
        receiver = get_object_or_404(User, id=receiver_id)

        # Check if a friend request already exists between the requester and receiver
        existing_request = FriendRequest.objects.filter(requester=requester, receiver=receiver).first()
        if existing_request:
            raise ValidationError({"detail": "Friend request already sent to this user."})

        # Create the friend request
        serializer.save(requester=requester, receiver=receiver, status=FriendRequest.PENDING)

#Get all friend requests
class FriendRequestListView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter()
