from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Todo(models.Model):
    todo_name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    parent_todo = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    priority = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '<{} ({})>'.format(self.todo_name, self.priority)

    def info_dict(self):
        info_dict = self.__dict__.copy()
        info_dict.update({
            'child_list': self.todo_list(self),
        })
        del info_dict['_state'], info_dict['parent_todo_id']

        return info_dict

    @classmethod
    def todo_list(cls, parent_id=None):
        todo_list = Todo.objects.filter(parent_todo=parent_id).order_by('pub_date')

        return [todo.info_dict() for todo in todo_list]

    def partial_update(self, request):
        self.__dict__.update(request.POST.items())

        # parse priority
        if self.priority == '':
            self.priority = None

        # parse parent_todo
        if 'parent_todo' in self.__dict__:
            self.parent_todo_id = int(self.__dict__.pop('parent_todo'))
            if self.parent_todo_id == self.id:
                raise ValidationError('Invalid parent')
