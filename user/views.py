from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly


#Get all users
class UserListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return User.objects.filter(first_name__icontains=search)
        return User.objects.all()


#Get single user by id
class UserSingleView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#Delete and patch by id
"""
TODO: Send bearer token with patch request and delete request. Has to be done in the frontend, right?
"""
class RetrieveUpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]