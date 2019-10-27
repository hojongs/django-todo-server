from django.shortcuts import render


def index(request):
    return render(request, 'todo_list_client/index.html')


def detail(request, todo_id):
    return render(request, 'todo_list_client/detail.html')


def todo_form(request):
    return render(request, 'todo_list_client/todo_form.html')
