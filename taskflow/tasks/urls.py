from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/new/', views.task_create, name='task_create'),

    path(
        'tasks/<int:pk>/edit/',
        views.task_update,
        name='task_update'
    ),
]