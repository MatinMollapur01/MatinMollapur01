from django.contrib import admin
from django.urls import path
from tasks.views import task_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
]
