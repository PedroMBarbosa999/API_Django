from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import Task, User
from .serializer import TaskSerializer


class TaskSerializerTests(TestCase):
    def test_task_serializer_imports_task_model(self):
        self.assertTrue(hasattr(TaskSerializer, 'Meta'))
        self.assertEqual(TaskSerializer.Meta.model.__name__, 'Task')


class TaskDetailViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(name='Ana', email='ana@example.com', password='123456')
        self.task = Task.objects.create(
            title='Estudar Django',
            description='Revisar views',
            status=0,
            user_id=self.user,
        )

    def test_get_task_detail_returns_task_data(self):
        response = self.client.get(reverse('task_detail', args=[self.task.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.task.title)

    def test_delete_task_detail_removes_task(self):
        response = self.client.delete(reverse('task_detail', args=[self.task.pk]))

        self.assertEqual(response.status_code, 204)
        self.assertFalse(Task.objects.filter(pk=self.task.pk).exists())

    def test_get_tasks_by_user_returns_only_user_tasks(self):
        another_user = User.objects.create(name='Bruno', email='bruno@example.com', password='654321')
        Task.objects.create(
            title='Fazer exercício',
            description='Correr',
            status=1,
            user_id=another_user,
        )

        response = self.client.get(reverse('tasks_by_user', args=[self.user.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.task.title)
