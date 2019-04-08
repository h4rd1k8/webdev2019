from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api import models
# Create your views here.


def task_lists(request):
    t_lists = models.TaskList.objects.all()
    json_t_lists = [t.to_json() for t in t_lists]
    return JsonResponse(json_t_lists, safe=False)


def task_list(request, pk):
    try:
        t_list = models.TaskList.objects.get(id=pk)
    except models.TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    return JsonResponse(t_list.to_json(), safe=False)


def task_lists_tasks(request, pk):
    try:
        t_list = models.TaskList.objects.get(id=pk)
    except models.TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False)

    tasks = t_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    #return HttpResponse('<h1>{}</h1>'.format(json_tasks))
    return JsonResponse(json_tasks, safe=False)
