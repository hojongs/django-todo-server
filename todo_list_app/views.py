import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader

from .models import Todo
from .forms import TodoForm


def index(request):
    template = loader.get_template('todo_list_app/index.html')
    ctxt = {'todo_list': Todo.todo_list()}

    return HttpResponse(template.render(ctxt, request))


def detail(request, todo_id):
    return HttpResponse("detail page of %d" % todo_id)


def modify(request):
    try:
        todo = Todo.objects.get(id=request.GET.get('id'))
    except Exception as e:
        todo = None

    if request.method == 'GET':
        # init form
        if todo:
            form = TodoForm(instance=todo)
        else:
            parent_todo = request.GET.get('parent_todo')
            form = TodoForm(initial={'parent_todo': parent_todo})
    else:
        print('POST', request.POST)
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return HttpResponseRedirect('/')

    return render(request, 'todo_list_app/modify.html', {'form': form})


def modify_action(request):
    values = request.GET.dict()
    print('values', values)
    todo = Todo.objects.get(id=values.pop('todo_id'))
    print(todo)
    todo.__dict__ = values
    print(todo)

    return HttpResponse(todo)


def todo_tree(request):
    return JsonResponse({'tree': Todo.todo_list()})
