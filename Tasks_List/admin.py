from django.contrib import admin
from Tasks_List.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_name", "description", "current_date", "end_date")

admin.site.register(Task, TaskAdmin)