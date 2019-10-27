import logging
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest

from .models import Todo
from .forms import TodoForm

logger = logging.getLogger(__name__)


def todo(request):
    if request.method == 'GET':
        return todo_list(request)
    elif request.method == 'POST':
        return create_todo(request)
    else:
        return HttpResponseForbidden()


def todo_list(request):
    parent_id = request.GET.get('parent_id')
    logger.info('[todo_list] parent_id=%s', parent_id)

    return JsonResponse({'todo_list': Todo.todo_list(parent_id=parent_id)})


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save()
            logger.info('[create] created todo=%s', todo)

            return JsonResponse(todo.info_dict())

    return HttpResponseForbidden()


def todo_detail(request, todo_id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=todo_id)

            return JsonResponse(todo.info_dict())
        except Exception as e:
            return HttpResponseBadRequest('Wrong Todo ID')
    elif request.method == 'POST':
        return update_todo(request, todo_id)
    else:
        return HttpResponseForbidden()


def update_todo(request, todo_id):
    if request.method == 'POST':
        try:
            logger.info('[update_todo] todo_id=%s', todo_id)
            todo = Todo.objects.get(id=todo_id)

            todo.__dict__.update(request.POST.items())
            todo.save()

            return JsonResponse(todo.info_dict())
        except Exception as e:
            logger.error(e)
            return HttpResponseBadRequest('Wrong Todo ID')


def todo_form(request):
    todo_id = request.GET.get('todo_id')
    try:
        todo = Todo.objects.get(id=todo_id)
    except:
        todo = None

    logger.info('[todo_form] todo_id=%s, todo=%s', todo_id, todo)
    f = TodoForm(instance=todo)
    return HttpResponse(str(f))


def delete(request):
    if request.method == 'POST':
        delete_id = int(request.POST.get('delete_id'))
        logger.info('[delete] %d', delete_id)
        try:
            todo = Todo.objects.get(id=delete_id)
            todo.delete()

            return HttpResponseRedirect('/')
        except Exception as e:
            logger.error('[delete] %s', e)

    return HttpResponseForbidden()
