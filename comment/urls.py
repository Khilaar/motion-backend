from django.urls import path
from .views import ListCommentsView

urlpatterns = [
    path('<int:post_id>', ListCommentsView.as_view()),
]