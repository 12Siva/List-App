from django.db import models

# Create your models here.
class Task(models.Model):
    # Task
    task_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    current_date = models.DateTimeField('Current Date')
    end_date = models.DateTimeField('End Date')