from django.contrib import admin

# Register your models here.

from .models import Task, Project, Comment

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)