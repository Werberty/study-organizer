from django.shortcuts import render

from .forms import LoginForm, RegisterForm


def register(request):
    form = RegisterForm()

    return render(request, 'accounts/pages/register.html', context={
        'form': form
    })


def login(request):
    form = LoginForm()

    return render(request, 'accounts/pages/login.html', context={
        'form': form
    })
