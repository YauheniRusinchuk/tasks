from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from src.models.boards.models import Board



class NewTaskView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home/new.html', {})




class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html', {})


    def post(self, request, *args, **kwargs):
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home_page')
        else:
            return redirect('home:login_page')


def log_out(request):
    logout(request)
    return redirect('/')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/index.html', {})
    boards = Board.objects.filter(user=request.user)
    return render(request, 'home/index.html', {'boards': boards})
