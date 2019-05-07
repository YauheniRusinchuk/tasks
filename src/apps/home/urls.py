from django.urls import path
from .views import index, LoginView, log_out


app_name = 'home'


urlpatterns = [
    path('', index, name='home_page'),
    path('exit/', log_out, name='logout_page'),
    path('login/', LoginView.as_view(), name='login_page'),
]
