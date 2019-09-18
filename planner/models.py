from django.db import models
from django.contrib.auth.models import User

from eventtools.models import BaseEvent, BaseOccurrence



class Schedule():
    """
    Users:
    There could be multiple users that share a task list.
    A user only has one task list that they are associated with,
    although this is not a necessity.

    Events:
    A task list stores all events for a user group.
    Occurrences are thereby owned indirectly as well.

    """
    users = models.ManyToManyField(User, through='ScheduleUser')


class ScheduleUser(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    # temporary - users can only have one organisation for now
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Task():
    title = models.CharField(max_length=100)
    details =  models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    points = models.IntegerField(default=10)


class Event(BaseEvent):
    """
    A Task can have multiple event schedules.
    This is for in case a recurring task is to happen twice a week.
    This is necessary because events are only daily, weekly, monthly etc.

    Since there are multiple events per Task, the events point to parent Task. 
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


class Occurrence(BaseOccurrence):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
