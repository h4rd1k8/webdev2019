from api.models import TaskList
from api.serializers import TaskListSerializer, TaskSerializer 
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.pagination import PageNumberPagination
from api.filters import TaskListFilter, TaskFilter


class TaskListsAPIView(generics.ListCreateAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # pagination_class = LimitOffsetPagination
    # filterset_fields = ('name',)
    filter_class = TaskListFilter
    search_fields = ('name',)
    ordering_fields = ('name',)
    ordering = ('name',)

    def get_queryset(self):
        return TaskList.objects.for_user(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TaskListAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TaskList.objects.for_user(user=self.request.user)


class TaskListTasksAPIView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_class = TaskFilter
    # pagination_class = LimitOffsetPagination
    search_fields = ('name', 'status', 'created_at')
    ordering_fields = ('name', 'status', 'created_at')
    ordering = ('created_at',)

    def get_queryset(self):
        try:
            task_list = TaskList.objects.for_user(user=self.request.user).get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404
        return task_list.task_set.all()

    def perform_create(self, serializer):
        try:
            task_list = TaskList.objects.get(id=self.kwargs['pk'])
        except TaskList.DoesNotExist:
            raise Http404
        serializer.save(task_list=task_list)


# class TaskListTaskAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = TaskSerializer
#     permission_classes = (IsAuthenticated,)

#     def get_queryset(self):
#         print(self.kwargs)
#         return Task.objects.for_user(user=self.request.user, pk1=self.kwargs['pk'])
    
#     def get_serializer_class(self):
#         return TaskSerializer
# TODO add  permissions(filter), some filter, search, ordering, pagination
