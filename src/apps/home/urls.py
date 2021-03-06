from django.urls import path
from .views import (
    index,
    LoginView,
    log_out,
    NewTaskView,
    DeleteTaskView
)


app_name = 'home'


urlpatterns = [
    path('', index, name='home_page'),
    path('delete/<int:pk>/', DeleteTaskView.as_view(), name='delete_task'),
    path('newtask/', NewTaskView.as_view(), name='new_page'),
    path('exit/', log_out, name='logout_page'),
    path('login/', LoginView.as_view(), name='login_page'),
]
