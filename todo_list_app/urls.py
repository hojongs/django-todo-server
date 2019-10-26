from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('modify/', views.modify, name='modify'),
    path('modify/action/', views.modify_action, name='modify_action'),
    path('todo_tree/', views.todo_tree, name='todo_tree'),
]
