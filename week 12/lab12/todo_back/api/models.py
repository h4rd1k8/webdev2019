
# Create your models here.
from django.db import models


class TaskList(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    due_on = models.DateTimeField(auto_now=False)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
