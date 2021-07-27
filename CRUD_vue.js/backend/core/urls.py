from django.urls import path
from .views import TodoListView,TodoDetailView,search_todo
urlpatterns = [
    path('',TodoListView.as_view()),
    path('todo/<int:pk>',TodoDetailView.as_view()),
    path('search/<str:task>',search_todo)
]