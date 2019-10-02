from django.contrib import admin
from .models import Schedule, Task, Person



class TaskInline(admin.TabularInline):
    model = Task

class ScheduleAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]

class PersonAdmin(admin.ModelAdmin):
    inlines = [
        TaskInline,
    ]

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Task)
admin.site.register(Person, PersonAdmin)