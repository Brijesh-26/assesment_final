from rest_framework import serializers
from .models import Todo

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['title', 'desc', 'isDone', 'date']