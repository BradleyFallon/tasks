from django.contrib import admin
from .models import MyEvent, MyOccurrence

admin.site.register(MyEvent)
admin.site.register(MyOccurrence)