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
    try:
        todo = Todo.objects.get(id=todo_id)
    except Exception as e:
        return HttpResponseRedirect('/')

    template = loader.get_template('todo_list_app/detail.html')
    ctxt = {'todo': todo}
    return HttpResponse(template.render(ctxt, request))


def modify(request):

    if request.method == 'GET':
        # init form
        try:
            todo = Todo.objects.get(id=request.GET.get('id'))
            form = TodoForm(instance=todo)
        except Exception as e:
            parent_todo = request.GET.get('parent_todo')
            form = TodoForm(initial={'parent_todo': parent_todo})
    else:
        try:
            todo = Todo.objects.get(id=request.POST.get('id'))
            form = TodoForm(request.POST, instance=todo)
        except Exception as e:
            form = TodoForm(request.POST)
            
        if form.is_valid():
            todo = form.save()
        return HttpResponseRedirect('/')

    return render(request, 'todo_list_app/modify.html', {'form': form})


def todo_tree(request):
    return JsonResponse({'tree': Todo.todo_list()})


def delete(request):
    print(request.POST)
    todo_id = request.POST.get('id')
    try:
        todo = Todo.objects.get(id=todo_id)
        todo.delete()
    except Exception as e:
        pass

    return HttpResponseRedirect('/')
