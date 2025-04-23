from rest_framework import serializers
from ..models import Task
from .tag import TagSerializer

class TaskSerializer(serializers.ModelSerializer):
    tags  = TagSerializer(many=True, read_only=True)
    class Meta:
        model  = Task
        fields = ['id','title','details','is_done','tags','created','updated']
