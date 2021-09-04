from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path("todo-detail/<int:pk>/", DetailTodo.as_view() ),
    path('todo-list/', ListTodo.as_view())
]