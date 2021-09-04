from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http import Http404
from django.shortcuts import get_object_or_404


from .models import Todo
from .serializers import TodoSerializer

class ListTodo(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'put', 'delete']
    
    def get(self, request, format=None):
        user = request.user
        data = Todo.objects.filter(user = user)
        serializer = TodoSerializer(data, many=True)
        content = {
            'user':user.email,
            'status': 'request was permitted',
            'data':serializer.data
        }
        return Response(content)
    
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailTodo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response({'message':'Data Has Been Deleted'})