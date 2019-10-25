import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Todo


def index(request):
    template = loader.get_template('todo_list_app/index.html')
    ctxt = {'todo_list': Todo.todo_list()}

    return HttpResponse(template.render(ctxt, request))


def detail(request, todo_id):
    return HttpResponse("detail page of %d" % todo_id)


def modify(request, todo_id):
    return HttpResponse("modify page of %d" % todo_id)


def todo_tree(request):
    return JsonResponse({'tree': Todo.todo_list()})
