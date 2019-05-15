from rest_framework import serializers
from api.models import TaskList, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TaskListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = TaskList
        fields = ('id', 'name', 'created_by',)
    # def create(self, validated_data):
    #     task_list = TaskList(**validated_data)
    #     task_list.save()
    #     return task_list
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    task_list = TaskListSerializer()
    created_at = serializers.DateTimeField(required=False)
    due_on = serializers.DateTimeField(required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.due_on = validated_data.get('due_on', instance.due_on)
        instance.status = validated_data.get('status', instance.status)
        instance.task_list = validated_data.get('task_list', instance.task_list)
        instance.save()
        return instance
