from rest_framework import serializers
from api.models import TaskList, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        

class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_by = UserSerializer(required=False)

    class Meta:
        model = TaskList
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list = TaskListSerializer(required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.status = validated_data.get('status', instance.status)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.due_on = validated_data.get('due_on', instance.due_on)
        instance.save()
        return instance

