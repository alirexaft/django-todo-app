from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, delete_task, updatetask

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('update_task/<str:pk>/', updatetask, name="update_task"),
]
