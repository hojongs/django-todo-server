from django.db import models


class Todo(models.Model):
    todo_name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    parent_todo = models.ForeignKey('self', on_delete=models.CASCADE)
    priority = models.IntegerField()
