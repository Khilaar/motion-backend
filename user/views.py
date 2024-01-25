from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly

########################################################################################

#Get all users
class UserListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        if search:
            return User.objects.filter(first_name__icontains=search)
        return User.objects.all()

########################################################################################

#Get single user by id
class UserSingleView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

########################################################################################

#Get logged in user (me)
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

########################################################################################

#Patch logged in user (me)
class CurrentUserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


########################################################################################

#Delete and patch by id
#Authorization added, can only patch and delete own user profile
class RetrieveUpdateDeleteUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]

########################################################################################

#Follow another user
class FollowUserView(APIView):
    def post(self, request, pk):
        user = request.user

        if user.pk == pk:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        user_to_follow = get_object_or_404(User, pk=pk)

        if user_to_follow in user.user_following.all():
            return Response({'detail': 'You are already following this user.'}, status=status.HTTP_400_BAD_REQUEST)

        user.user_following.add(user_to_follow)
        return Response({'detail': 'You are now following this user.'}, status=status.HTTP_200_OK)
