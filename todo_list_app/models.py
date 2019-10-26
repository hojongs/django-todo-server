from django.db import models
from django.utils import timezone


class Todo(models.Model):
    todo_name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    parent_todo = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.todo_name, self.priority)

    @classmethod
    def todo_list(cls, parent=None):
        tree = []
        parent = parent.id if parent else None

        todo_list = Todo.objects.filter(parent_todo=parent).order_by('pub_date')
        import collections
        for todo in todo_list:
            tree.append(dict({
                'id': todo.id,
                'todo_name': todo.todo_name,
                'pub_date': todo.pub_date,
                'child_list': cls.todo_list(todo),
            }))

        return tree
