from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:todo_id>/', views.detail, name='detail'),
    path('todo_form/', views.todo_form, name='todo_form'),
]
