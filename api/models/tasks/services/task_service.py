from ..repositories.task_repository import TaskRepository

class TaskService:
    @staticmethod
    def list_for_user(user):
        return TaskRepository.for_user(user)

    @staticmethod
    def create_task(owner, **payload):
        return TaskRepository.create(owner, **payload)
