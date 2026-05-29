from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskForm

def home(request):
    """
    Render the homepage.
    """

    return render(request, 'home.html')


@login_required
def dashboard(request):
    """
    Render the logged-in user's dashboard.
    """

    return render(request, 'dashboard.html')


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