from django.db import models
from django.utils import timezone


class Todo(models.Model):
    todo_name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    parent_todo = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.todo_name
