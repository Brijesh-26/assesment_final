from .models import Todo
from .serializers import SnippetSerializer
from rest_framework import generics


class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = SnippetSerializer


class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = SnippetSerializer