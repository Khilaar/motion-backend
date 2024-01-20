from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from .models import User
from .serializers import UserSerializer

class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return User.objects.filter(first_name__icontains=search)
        return User.objects.all()


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer