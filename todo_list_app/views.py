from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("todo_list_app index")


def detail(request, todo_id):
    return HttpResponse("detail page of %d" % todo_id)


def modify(request, todo_id):
    return HttpResponse("modify page of %d" % todo_id)
