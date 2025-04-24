from rest_framework import generics, permissions
from ..models import Task
from ..serializers.task import TaskSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET   /tasks/<pk>/      → retrieve one task
    PUT   /tasks/<pk>/      → full update
    PATCH /tasks/<pk>/      → partial update
    DELETE /tasks/<pk>/     → delete
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
