from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.views import generic

from .models import Task, Schedule

def index(request):
    return HttpResponse("Hello, world. You're at the planner index.")


class ChecklistView(generic.DetailView):
    """
    Shows a list of all tasks that must be done, sorted by highest point value.
    
    Task A         1000 pts   <--- click a task to open task detail
    Task B         1000 pts
    Task C          400 pts
    Task D           30 pts
    """
    model = Schedule
    template_name = 'planner/checklist.html'


class TaskView(generic.DetailView):
    """
    Shows the task and the description and completion requirements.

    Take a picture to prove it option here.
    For simple prototype, just click done button.

    """
    model = Task
    template_name = 'planner/task_detail.html'


def done_list():
    """
    Show the list of all tasks done and their value and all badges earned today
    """
    return None

def badge_history():
    """
    Shows a left-right scrolling columns containing the badges earned in past days.

    Shows the total number of badges earned of each type.

    Shows the rewards that are yet to be redeemed.
    """
    return None

