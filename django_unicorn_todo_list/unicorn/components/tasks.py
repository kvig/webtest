from django_unicorn.components import UnicornView
from lists.models import List, Task


class TasksView(UnicornView):
    title: str = ""
    completed: bool = False
    parent_list: List = None
    tasks = Task.objects.none()

    def hydrate(self):
        self.tasks = Task.objects.filter(parent_list__user=self.request.user)

    def add_task(self):
        new_task = Task(title=self.title, completed=self.completed, parent_list=self.parent_list)
        new_task.save()
        self.title = ""
        self.completed = False

    def toggle_complete(self, task_id):
        task = self.tasks.get(pk=task_id)
        task.completed = not task.completed
        task.save()

    def delete(self, id):
        Task.objects.get(pk=id).delete()
        self.tasks = self.tasks.exclude(pk=id)
