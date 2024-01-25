from django.urls import path
from .views import SendFriendRequestView, FriendRequestListView, SentFriendRequestListView, \
    ReceivedFriendRequestListView

urlpatterns = [
    path('request/<int:pk>/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('allrequests', FriendRequestListView.as_view(), name='all-requests'),
    path('sentrequests', SentFriendRequestListView.as_view(), name='sent-requests'),
    path('receivedrequests', ReceivedFriendRequestListView.as_view(), name='received-requests')
]