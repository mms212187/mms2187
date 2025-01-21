

from django.contrib import admin
from .models import Project, Task

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'start_date', 'end_date')
    list_filter = ('status',)
    search_fields = ('name', 'description')

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'priority', 'status', 'start_date', 'end_date')
    list_filter = ('priority', 'status', 'project')
    search_fields = ('name', 'description')




