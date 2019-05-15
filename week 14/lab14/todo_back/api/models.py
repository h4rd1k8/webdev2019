from django.db import models
from django.contrib.auth.models import User


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user)


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = TaskListManager()

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'        


class TaskManager(models.Manager):
    def for_user(self, pk1, pk2, user):
        return TaskList.objects.for_user(user=user).get(id=pk1).task_set.get(id=pk2)
        

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, editable=True)
    due_on = models.DateTimeField(auto_now=False, editable=True)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    objects = TaskManager()

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
