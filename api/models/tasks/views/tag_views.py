from rest_framework import generics, permissions
from ..models import Tag
from ..serializers.tag import TagSerializer

class TagListCreateAPIView(generics.ListCreateAPIView):
    serializer_class   = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

