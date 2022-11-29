from django.shortcuts import render

from .forms import RegisterForm


def register(request):
    form = RegisterForm()

    return render(request, 'accounts/pages/register.html', context={
        'form': form
    })
