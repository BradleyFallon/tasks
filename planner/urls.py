from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('c<int:checklist_id>/', views.ChecklistView.as_view(), name='checklist'),
    path('c<int:checklist_id>/t<int:task_id>/', views.TaskView.as_view(), name='task_detail'),
    path('t<int:pk>/', views.TaskView.as_view(), name='task_detail'),
    path('t/', views.TaskListView.as_view(), name='task_list'),
    path('today/', views.TaskListToday.as_view(), name='today'),
    path('new/', views.new_task, name='new_task'),
]

