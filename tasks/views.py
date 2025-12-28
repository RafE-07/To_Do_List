from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def task_list(request):
    task=Task.objects.all()
    context = {'task': task}
    return render(request, 'tasks/task_list.html', context)

def add_task(request):
    return HttpResponse("Add Task View")

def home(request):
    return render(request, 'tasks/base.html')