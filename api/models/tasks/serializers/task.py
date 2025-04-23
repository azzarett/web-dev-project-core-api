from rest_framework import serializers
from ..models import Task, Tag
from .tag import TagSerializer

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Tag.objects.all(),
        source='tags'
    )

    class Meta:
        model  = Task
        fields = ['id', 'title', 'details', 'is_done', 'tags', 'tag_ids', 'created', 'updated',]