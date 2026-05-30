from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    """
    Form for creating and updating tasks.
    """

    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'status', 'due_date']

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }