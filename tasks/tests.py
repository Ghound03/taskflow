from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Task


class TaskModelTest(TestCase):
  

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_task_creation(self):
       

        task = Task.objects.create(
            title='Test Task',
            description='Testing task creation',
            priority='High',
            status='Pending',
            due_date='2026-06-30',
            owner=self.user
        )

        self.assertEqual(task.title, 'Test Task')


class DashboardViewTest(TestCase):
   

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_dashboard_requires_login(self):
       

        response = self.client.get(
            reverse('dashboard')
        )

        self.assertEqual(
            response.status_code,
            302
        )

    def test_dashboard_logged_in(self):

        self.client.login(
            username='testuser',
            password='testpass123'
        )

        response = self.client.get(
            reverse('dashboard')
        )

        self.assertEqual(
            response.status_code,
            200
        )
    

class TaskCreationViewTest(TestCase):
    """
    Test task creation.
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='creator',
            password='testpass123'
        )

    def test_create_task(self):

        self.client.login(
            username='creator',
            password='testpass123'
        )

        response = self.client.post(
            reverse('task_create'),
            {
                'title': 'Assignment',
                'description': 'Finish project',
                'priority': 'High',
                'status': 'Pending',
                'due_date': '2026-06-30'
            }
        )

        self.assertEqual(
            Task.objects.count(),
            1
        )

        self.assertEqual(
            response.status_code,
            302
        )