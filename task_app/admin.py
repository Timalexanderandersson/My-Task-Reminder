from django.contrib import admin
from .models import Taskmodel, Task
# Register your models here.

@admin.register(Taskmodel)
class Taskmodeladmin(admin.ModelAdmin):
    list_display = ("user", "name")
    

@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ("task_list", "description","completed","due_date")
