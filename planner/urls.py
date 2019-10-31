from django.urls import path

from . import views

app_name = 'planner'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('t<int:pk>/', views.TaskView.as_view(), name='task_detail'),
    path('t/', views.tasks_page, name='task_list'),
    path('new/', views.new_task, name='new_task'),
]

