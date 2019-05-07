from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'auth/login.html', {})



def log_out(request):
    logout(request)
    return redirect('/')


def index(request):
    return render(request, 'home/index.html', {})
