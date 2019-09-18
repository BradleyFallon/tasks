from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.index, name='index'),
    path('c<int:checklist_id>/', views.ChecklistView.as_view(), name='checklist'),
    path('c<int:checklist_id>/t<int:task_id>/', views.TaskView.as_view(), name='task_detail'),
]

