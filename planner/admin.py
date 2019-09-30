from django.contrib import admin
from .models import Schedule, Task, Event, Occurrence



class TaskInline(admin.TabularInline):
    model = Task

class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]


class EventInline(admin.TabularInline):
    model = Event

class TaskAdmin(admin.ModelAdmin):
    inlines = [
        EventInline,
    ]

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Event)
admin.site.register(Occurrence)