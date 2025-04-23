from ..models import Task

class TaskRepository:
    @staticmethod
    def for_user(user):
        return Task.objects.filter(owner=user)

    @staticmethod
    def create(owner, **data):
        return Task.objects.create(owner=owner, **data)
