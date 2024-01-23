from .models import Post
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ListCreatePostView(ListCreateAPIView):
    """
    get: This endpoint lists all Posts
    or filters them by search or item_name query params
    post: Create an Post for the logged in user
    """
    # queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        search = self.request.query_params.get('search')
        item_name = self.request.query_params.get('item_name')
        if item_name:
            return Post.objects.filter(items__name__icontains=item_name)

        if search:
            return Post.objects.filter(customer_text__icontains=search)
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListLoggedInUserPosts(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class RetrieveUpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
