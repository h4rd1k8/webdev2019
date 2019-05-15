from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer 
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskListTaskAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get_task(self, request, pk1, pk2):
        try:
            task = TaskList.objects.for_user(user=request.user).get(id=pk1).task_set.get(id=pk2)
        except:
            raise Http404
        return task
    
    def get(self, request, pk1, pk2):
        task = self.get_task(request, pk1, pk2)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk1, pk2):
        task = self.get_task(request, pk1, pk2)
        try:
            request.data.pop('task_list')
        except:
            pass    
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk1, pk2):
        task = self.get_task(request, pk1, pk2)
        task.delete()
        return Response({"delete_status": "successful"})