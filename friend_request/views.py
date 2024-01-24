from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from .models import FriendRequest
from .serializers import FriendRequestSerializer
from django.shortcuts import get_object_or_404

User = get_user_model()

"""
TODO:
At the moment the current user can send mulitple request to each user.
"""


# Create your views here.
class SendFriendRequestView(CreateAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        receiver_id = self.kwargs['pk']
        receiver = get_object_or_404(User, id=receiver_id)
        serializer.save(requester=self.request.user, receiver=receiver, status=FriendRequest.PENDING)


#Get all friend requests
class FriendRequestListView(ListAPIView):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter()
