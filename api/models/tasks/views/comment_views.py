from rest_framework import generics, permissions
from ..models import Comment
from ..serializers.comment import CommentSerializer

class CommentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class   = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_pk'])

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        task_id=self.kwargs['task_pk'])
