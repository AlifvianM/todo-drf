from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from django.http import Http404
from django.shortcuts import get_object_or_404


from .models import Todo
from .serializers import TodoSerializer

class ListTodo(ListCreateAPIView):
    http_method_names = ['get', 'post']	
    permission_classes = [IsAuthenticated]    
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(user = user)
        return queryset

class DetailTodo(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()