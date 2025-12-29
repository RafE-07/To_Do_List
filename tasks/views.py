from django.shortcuts import render, redirect, get_object_or_404

from .models import Task


# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, "tasks/task_list.html", context)


def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        Task.objects.create(title=title)
    return redirect("tasks:task_list")


def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        title = request.POST.get("title", "")
        task.title = title
        task.save()
        return redirect("tasks:task_list")
    return render(request, "tasks/task_edit.html", {"task": task})


def toggle_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = not task.completed
    task.save()
    return redirect("tasks:task_list")


def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    return redirect("tasks:task_list")