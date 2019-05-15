from django_filters import rest_framework as filters
from api.models import TaskList, Task


class TaskListFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TaskList
        fields = ('name',)


class TaskFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')
    status = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Task
        fields = ('name', 'status',)

