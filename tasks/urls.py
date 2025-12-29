from django.urls import path

from . import views

app_name = 'tasks'

urlpatterns = [
    path('task_list/', views.task_list, name='task_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('delete_task/<int:id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:id>/', views.edit_task, name='edit_task'),
    path('toggle_task/<int:id>/', views.toggle_task, name='toggle_task'),
]
