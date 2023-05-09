from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('tasks', views.task_list, name='task-list-complete'),
    path('tasks/', views.task_list, name='task-list-filtered'),
    path('tasks/<int:pk>', views.task_details, name='task-by-id'),
    path('history', views.get_history_list, name='history-list-complete'),
    path('history/', views.get_history_list, name='history-list-filtered'),
    path('register', views.register_request, name='user-creation'),
    path('login', views.login_request, name='user-login'),
]