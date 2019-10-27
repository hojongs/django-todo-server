from django.urls import path

from . import views

urlpatterns = [
    path('todo/', views.todo, name='todo'),
    path('todo/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('todo_form/', views.todo_form, name='todo_form'),
    path('delete/', views.delete, name='delete'),
]
