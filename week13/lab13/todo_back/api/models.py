
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class TaskListManager(models.Manager):
    def for_user(self, user):
        return self.filter(created_by=user).order_by('name')

    # def get_today(self, date):
    #     return self.filter(created_at.year=data.year,
    #                     created_at.month = data.month,
    #                     created_at.day = data.day)


class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    objects = TaskListManager()

    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
