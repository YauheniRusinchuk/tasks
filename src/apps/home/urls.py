from django.urls import path
from .views import index, LoginView, log_out, NewTaskView


app_name = 'home'


urlpatterns = [
    path('', index, name='home_page'),
    path('newtask/', NewTaskView.as_view(), name='new_page'),
    path('exit/', log_out, name='logout_page'),
    path('login/', LoginView.as_view(), name='login_page'),
]
