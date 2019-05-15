from django.urls import path
from api import views

urlpatterns = [
    path('api/users/', views.UserList.as_view()),
    path('api/login/', views.login),
    path('api/logout/', views.logout),
    path('api/task_lists/', views.TaskListsView.as_view()),
    path('api/task_lists/<int:pk>/', views.TaskListView.as_view()),
    path('api/task_lists/<int:pk2>/tasks/<int:pk>/', views.TaskListTaskView.as_view()),
    path('api/task_lists/<int:pk>/tasks/', views.TaskListTasksView.as_view())
]

