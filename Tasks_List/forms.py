from django import forms
from Tasks_List.models import Task

class Task_Form(forms.ModelForm):
    task_name = forms.CharField(max_length=200, help_text="Task Name")
    description = forms.CharField(max_length=200, help_text="Description", required=False)
    current_date = forms.DateTimeField(help_text="Start Date")
    end_date = forms.DateTimeField(help_text="Due Date")

    class Meta:
        model = Task

