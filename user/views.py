from rest_framework.generics import ListAPIView, ListCreateAPIView
from .models import User
from .serializers import UserSerializer

class UserListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
