from django.urls import path
from api import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('task_lists/', views.TaskListsAPIView.as_view()),
    path('task_lists/<int:pk>/', views.TaskListAPIView.as_view()),
    path('task_lists/<int:pk>/tasks/', views.TaskListTasksAPIView.as_view()),
    path('task_lists/<int:pk1>/tasks/<int:pk2>/', views.TaskListTaskAPIView.as_view())
]