from django.shortcuts import render
from .models import Comment
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .serializers import CommentSerializer
from rest_framework import filters

# api/social/comments/<int:post_id>/ GET: List all comments of a post
class ListCommentsView(ListCreateAPIView):

    """Lists all comments related to a post."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['post_id']

    def get_query(self):
        current_post = self.request.query_params.get('post_id')
        return Comment.objects.filter(current_post = self.request.post)

    def perform_create(self, serializer):
        current_post = self.request.query_params.get('post_id')
        serializer.save(current_post = self.request.post)