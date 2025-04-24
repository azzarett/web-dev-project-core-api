from rest_framework import serializers
from ..models import Task, Tag
from .tag import TagSerializer

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        write_only=True,
        queryset=Tag.objects.all(),
        required=False,  # Сделать необязательным
        allow_null=True   # Разрешить null значения
    )
    title = serializers.CharField(required=False, allow_blank=True)  # Сделать необязательным

    class Meta:
        model = Task
        fields = ['id', 'title', 'details', 'is_done', 'tags', 'tag_ids', 'created', 'updated']
        read_only_fields = ['created', 'updated']  # Поля, которые не изменяются

    def update(self, instance, validated_data):
        # Обновляем теги, если они переданы
        tag_ids = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)

        # Если tag_ids были переданы, обновляем их
        if tag_ids is not None:
            instance.tags.set(tag_ids)

        return instance
