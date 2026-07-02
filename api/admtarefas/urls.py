from django.urls import path
from .views import users_list, user_detail

urlpatterns = [
    path('users/', users_list, name='users_list'),
    path('users/<int:pk>', user_detail, name='user_detail'),
]
