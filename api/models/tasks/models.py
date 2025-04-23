from django.db import models
from django.conf import settings

class Tag(models.Model):
    name       = models.CharField(max_length=30, unique=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tags', null=True, blank=True)
    def __str__(self): return self.name


class Task(models.Model):
    owner   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title   = models.CharField(max_length=120)
    details = models.TextField(blank=True)
    is_done = models.BooleanField(default=False)
    tags    = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title

class Comment(models.Model):
    task    = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
