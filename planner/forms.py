from django import forms

from .models import Task

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = (
            'title',
            'details',
            'points',
            # 'asignee',
            # 'schedule',
            # 'last_completed',
            'wait_days',
            )

