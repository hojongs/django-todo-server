import logging
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from .models import Todo
from .forms import TodoForm

logger = logging.getLogger(__name__)
json_dumps_params = {'ensure_ascii': False}


def todo(request):
    if request.method == 'GET':
        return todo_list(request)
    elif request.method == 'POST':
        return create_todo(request)
    else:
        return HttpResponseForbidden()


def todo_list(request):
    try:
        parent_id = request.GET.get('parent_id')
        if parent_id:
            parent_id = int(parent_id)
        logger.info('[todo_list] parent_id=%s', parent_id)

        return JsonResponse({'todo_list': Todo.todo_list(parent_id=parent_id)}, json_dumps_params=json_dumps_params)
    except ValueError as e:
        return HttpResponseBadRequest('invalid parent_id')


def create_todo(request):
    if request.method == 'POST':
        logger.info('[create_todo] request.POST=%s', request.POST)
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save()
            logger.info('[create_todo] created todo=%s', todo)

            return JsonResponse(todo.info_dict(), json_dumps_params=json_dumps_params)
        else:
            return HttpResponseBadRequest('invalid form data')

    return HttpResponseForbidden()


def todo_detail(request, todo_id):
    if request.method == 'GET':
        try:
            todo = Todo.objects.get(id=todo_id)

            return JsonResponse(todo.info_dict(), json_dumps_params=json_dumps_params)
        except ObjectDoesNotExist as e:
            return HttpResponseBadRequest('Wrong Todo ID')
    elif request.method == 'POST':
        return update_todo(request, todo_id)
    else:
        return HttpResponseForbidden()


def update_todo(request, todo_id):
    if request.method == 'POST':
        try:
            logger.info('[update_todo] todo_id=%s request.POST=%s', todo_id, request.POST)
            todo = Todo.objects.get(id=todo_id)
            todo.partial_update(request)

            logger.info('[update_todo] todo.__dict__=%s', todo.__dict__)
            todo.full_clean()  # validation of fields
            todo.save()
            return JsonResponse(todo.info_dict(), json_dumps_params=json_dumps_params)
        except ObjectDoesNotExist as e:
            logger.error(e)
            return HttpResponseBadRequest('Wrong Todo ID')
        except ValidationError as e:
            logger.error(e)
            return HttpResponseBadRequest('Invalid value of a field')


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
        try:
            delete_id = int(request.POST.get('delete_id'))
        except ValueError as e:
            logger.error(e)
            return HttpResponseBadRequest('invalid delete_id')

        logger.info('[delete] %d', delete_id)
        try:
            todo = Todo.objects.get(id=delete_id)
            todo.delete()

            return JsonResponse({'success': True}, json_dumps_params=json_dumps_params)
        except Exception as e:
            logger.error('[delete] %s', e)
            return HttpResponseBadRequest('invalid delete_id')

    return HttpResponseForbidden()
