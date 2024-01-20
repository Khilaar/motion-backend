from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from .models import User
from .serializers import UserSerializer

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer