import datetime

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.views import generic
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

from .models import Task, Schedule, Person
from .forms import TaskForm


@login_required()
def new_task(request):
    person = get_object_or_404(Person, user=request.user)
    schedule = get_object_or_404(Schedule, pk=person.schedule.pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.asignee = person
            task.schedule = schedule
            task.last_completed = datetime.date.today()
            task.save()
            return redirect('planner:today')
    else:
        form = TaskForm()
    return render(request, 'planner/new_task.html', {'form': form})


class LoginView(TemplateView):
    pass


class TaskListToday(LoginRequiredMixin, generic.ListView):
    template_name = 'planner/tasks.html'
    context_object_name = 'task_list'
    ordering = ['-points']

    def get_queryset(self):
        person = get_object_or_404(Person, user=self.request.user)
        return Task.objects.filter(asignee=person)


class Manager(TemplateView):
    pass

class questionaire(TemplateView):
    pass

class register(TemplateView):
    pass





















class HomePageView(TemplateView):
    template_name = "planner/index.html"


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


class TaskListView(generic.ListView):
    template_name = 'planner/tasks.html'
    context_object_name = 'task_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Task.objects.all()










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

