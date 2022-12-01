from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data') or None
    form = RegisterForm(register_form_data)

    return render(request, 'accounts/pages/register.html', context={
        'form': form
    })


def register_create(request):
    if request.method == 'POST':
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        form.set_password(user.password)
        form.save()

        del (request.session['register_form_data'])
        return redirect(reverse('studies:studies'))

    return redirect(reverse('accounts:register'))


def login(request):
    form = LoginForm()

    return render(request, 'accounts/pages/login.html', context={
        'form': form
    })
