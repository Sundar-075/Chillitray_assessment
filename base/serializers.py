from django.db.models import fields
from rest_framework import serializers
from .models import Tasks, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('uid', 'task_title', 'task_description', 'task_pic')
