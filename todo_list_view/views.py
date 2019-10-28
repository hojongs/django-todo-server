from django.shortcuts import render


def index(request):
    return render(request, 'todo_list_view/index.html')


def detail(request, todo_id):
    return render(request, 'todo_list_view/detail.html')


def todo_form(request):
    return render(request, 'todo_list_view/todo_form.html')
