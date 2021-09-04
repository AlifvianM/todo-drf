from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, max_length=100)
    # status = serializers.BooleanField(required=False)
    
    class Meta:
        model = Todo
        fields = ['id', 'name', 'status', 'created_at', 'updated_at']