from django.shortcuts import render
from django.contrib.auth.decorators import login_required


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
