from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoList
from .serializers import TodoListSerializer
from rest_framework import generics


class TodoListView(generics.ListCreateAPIView):
    queryset = TodoList.objects.all().order_by('-id')
    serializer_class = TodoListSerializer




class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


@api_view(['GET'])
def search_todo(request,task):
    tasks = TodoList.objects.filter(task__icontains=task).values()
    return Response(tasks)