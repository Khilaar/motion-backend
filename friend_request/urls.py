from django.urls import path
from .views import SendFriendRequestView, FriendRequestListView, SentFriendRequestListView, \
    ReceivedFriendRequestListView, SingleSentFriendRequestView, AcceptFriendRequestView, RejectFriendRequestView, \
    DeleteFriendRequestView

urlpatterns = [
    path('request/<int:pk>/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('allrequests/', FriendRequestListView.as_view(), name='all-requests'),
    path('sentrequests/', SentFriendRequestListView.as_view(), name='sent-requests'),
    path('receivedrequests/', ReceivedFriendRequestListView.as_view(), name='received-requests'),
    path('singlerequest/<int:pk>/', SingleSentFriendRequestView.as_view(), name='single-request'),
    path('accept/<int:pk>/', AcceptFriendRequestView.as_view(), name='accept-friend-request'),
    path('reject/<int:pk>/', RejectFriendRequestView.as_view(), name='reject-friend-request'),
    path('delete/<int:pk>/', DeleteFriendRequestView.as_view(), name='delete-friend-request')
]
