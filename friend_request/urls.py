from django.urls import path
from .views import SendFriendRequestView, FriendRequestListView

urlpatterns = [
    path('request/<int:pk>/', SendFriendRequestView.as_view(), name='send-friend-request'),
    path('allrequests', FriendRequestListView.as_view(), name='all-requests')
]