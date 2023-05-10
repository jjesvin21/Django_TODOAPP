from django.urls import path
from APP_TODO import views

urlpatterns = [
    path("todo/",views.ToDoTaskAPI.as_view()),
    path("todo/<int:id>/",views.TaskAPI.as_view()),
]
