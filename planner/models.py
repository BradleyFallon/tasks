from django.db import models
from django.contrib.auth.models import User

class Schedule(models.Model):
    """
    This is used to handle a collection of Persons and Tasks. 
    The schedule is the hub for connecting Persons into a group.
    When changing the Person associated with a Task, the Person choices are limited
    to those of the same Schedule as the editor.

    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    A "User" model just handles authentication. This is an extension upon that,
    in the form of a One-to-One relationship. This will connect a user with whatever
    data a user needs to use the app, such as permissions, groups, logs, object ownership etc.
    """
    # One-to-One link with a user account
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    title = models.CharField(max_length=100)
    details =  models.CharField(max_length=200)
    points = models.IntegerField(default=10)
    asignee = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL)
    schedule = models.ForeignKey(Schedule, null=True, blank=True, on_delete=models.SET_NULL)

    last_completed = models.DateTimeField('last completed')
    wait_days = models.IntegerField(default=1) # 1-->daily
    # to see if a task is due, round down to the beginning of day last_completed
    # then add datetime.timedelta(days=wait_days)
    # then check if the result is less than now

    def __str__(self):
        return self.title