"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todolist.views import (
    TaskCreateAPIView,
    TaskRetrieveAPIView,
    TaskListAPIView,
    TaskUpdateAPIView,
    TaskDestroyAPIView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/task/', TaskCreateAPIView.as_view(), name='task-create'),
    path('api/task/<int:pk>/', TaskRetrieveAPIView.as_view(), name='task-retrieve'),
    path('api/tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('api/task/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='task-update'),
    path('api/task/<int:pk>/delete/', TaskDestroyAPIView.as_view(), name='task-delete'),
]
