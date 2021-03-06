from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import DeleteView
from django.contrib.auth import authenticate, login, logout
from src.models.boards.models import Board
from django.contrib.auth.mixins import LoginRequiredMixin


class DeleteTaskView(View):

    def get(self, request, *args, **kwargs):
        task = Board.objects.get(pk=kwargs['pk'])
        if request.user == task.user:
            task.delete()
        return redirect('home:home_page')



class NewTaskView(LoginRequiredMixin,View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):
        return render(request, 'home/new.html', {})

    def post(self, request, *args, **kwargs):
        Board.objects.create(name=request.POST.get('text'), user=request.user)
        return redirect('/')




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
