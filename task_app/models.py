
from django.db import models
from django.contrib.auth.models import User

# Task list models
class Taskmodel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, related_name="tasklisting")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Task model 
class Task(models.Model):
    task_list = models.ForeignKey(
        Taskmodel, on_delete=models.CASCADE, related_name= "listoftask")
    description = models.TextField(max_length=300)   
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title