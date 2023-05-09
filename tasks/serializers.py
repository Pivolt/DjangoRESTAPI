from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, TaskHistory


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    
    class Meta:
        model = User
        fields = ['username', 'password']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    assigned_user = UserSerializer()
    class Meta:
        model = TaskHistory
        fields = '__all__'