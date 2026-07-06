from django.urls import path
from .views import task_detail, tasks_by_user, tasks_list, user_detail, user_login, users_list

urlpatterns = [
    path('users/', users_list, name='users_list'),
    path('users/<int:pk>', user_detail, name='user_detail'),
    path('users/login/', user_login, name='user_login'),
    path('tasks/', tasks_list, name='tasks_list'),
    path('tasks/<int:pk>', task_detail, name='task_detail'),
    path('tasks/user/<int:user_id>', tasks_by_user, name='tasks_by_user'),
]
