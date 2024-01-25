from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FriendRequest
from .serializers import FriendRequestSerializer
from django.shortcuts import get_object_or_404

User = get_user_model()

########################################################################################

#Send a friend request to a user
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

########################################################################################

#Get all friend requests from all users
class FriendRequestListView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter()

########################################################################################

#Get all friend requests that the current user sent
class SentFriendRequestListView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        current_user = self.request.user
        return FriendRequest.objects.filter(requester=current_user)

########################################################################################

#Get all friend requests that the current user received
class ReceivedFriendRequestListView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        current_user = self.request.user
        return FriendRequest.objects.filter(receiver=current_user)

########################################################################################

#Get a single friend request
class SingleSentFriendRequestView(RetrieveAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_object(self):
        friend_request_id = self.kwargs['pk']
        return get_object_or_404(FriendRequest, id=friend_request_id)

########################################################################################

#Accept a friend request
class AcceptFriendRequestView(APIView):
    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, id=pk)
        friend_request.status = FriendRequest.ACCEPTED
        friend_request.save()
        return Response({'detail': 'Friend request accepted.'})

########################################################################################

#Reject a friend request
class RejectFriendRequestView(APIView):
    def post(self, request, pk):
        friend_request = get_object_or_404(FriendRequest, id=pk)
        friend_request.status = FriendRequest.REJECTED
        friend_request.save()
        return Response({'detail': 'Friend request rejected.'})

########################################################################################