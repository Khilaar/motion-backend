from django.urls import path

from .views import ListCreatePostView, RetrieveUpdateDeletePostView

urlpatterns = [
    path('', ListCreatePostView.as_view()),
    path('<int:pk>/', RetrieveUpdateDeletePostView.as_view())
]