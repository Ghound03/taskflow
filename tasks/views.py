from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TaskForm
from .models import Task
import requests


def home(request):
    """
    Render the homepage.
    """

    return render(request, 'home.html')


@login_required
def dashboard(request):
    """
    Display and filter the user's tasks.
    """

    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    priority_filter = request.GET.get('priority', '')

    tasks = Task.objects.filter(
        owner=request.user
    ).order_by('due_date')

    if search_query:
        tasks = tasks.filter(
            title__icontains=search_query
        )

    if status_filter:
        tasks = tasks.filter(
            status=status_filter
        )

    if priority_filter:
        tasks = tasks.filter(
            priority=priority_filter
        )

    total_tasks = Task.objects.filter(
        owner=request.user
    ).count()

    pending_tasks = Task.objects.filter(
        owner=request.user,
        status='Pending'
    ).count()

    in_progress_tasks = Task.objects.filter(
        owner=request.user,
        status='In Progress'
    ).count()

    completed_tasks = Task.objects.filter(
        owner=request.user,
        status='Completed'
    ).count()

    quote = {
    'content': 'Small progress each day adds up to big results.',
    'author': 'TaskFlow'
     }

    try:
      response = requests.get(
        "https://api.quotable.io/random",
        timeout=5
    )

      if response.status_code == 200:
        data = response.json()

        quote = {
            'content': data['content'],
            'author': data['author']
        }

    except Exception:
         pass

    return render(
        request,
        'dashboard.html',
        {
            'tasks': tasks,
            'search_query': search_query,
            'status_filter': status_filter,
            'priority_filter': priority_filter,
            'total_tasks': total_tasks,
            'pending_tasks': pending_tasks,
            'in_progress_tasks': in_progress_tasks,
            'completed_tasks': completed_tasks,
            'quote': quote,
        }
    )


@login_required
def task_create(request):
    """
    Allow a logged-in user to create a new task.
    """

    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()

            return redirect('dashboard')

    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update(request, pk):
    """
    Update an existing task.
    """

    task = get_object_or_404(
        Task,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = TaskForm(instance=task)

    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
    )


@login_required
def task_delete(request, pk):
    """
    Delete an existing task.
    """

    task = get_object_or_404(
        Task,
        pk=pk,
        owner=request.user
    )

    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')

    return render(
        request,
        'tasks/task_confirm_delete.html',
        {'task': task}
    )