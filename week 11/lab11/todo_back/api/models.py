from django.db import models

# Create your models here.
from django.db import models
import datetime
from datetime import datetime as dt


class TaskList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = dt.now()
    due_on = dt.now() + datetime.timedelta(days=1)
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'created_at':self.created_at,
            'due_on': self.due_on
            #'task_list': self.task_list.to_json()
        }
