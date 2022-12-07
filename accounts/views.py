from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()

        messages.success(request, 'Cadastro sucedido')
        del (request.session['register_form_data'])
        return redirect(reverse('accounts:login'))

    messages.error(request, 'Erro no cadastro')
    return redirect(reverse('accounts:register'))


def login_view(request):
    form = LoginForm()

    return render(request, 'accounts/pages/login.html', context={
        'form': form
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    if form.is_valid():
        authenticated_user = authenticate(
            username=username,
            password=password
        )

        if authenticated_user is not None:
            messages.success(request, 'Logado com sucesso')
            login(request, authenticated_user)
            return redirect(reverse('studies:home'))
        else:
            messages.error(request, 'Usuário ou senha inválido')

    else:
        messages.error(request, 'Credenciais inválidas')

    return redirect(reverse('accounts:login'))


@login_required(login_url='accounts:login', redirect_field_name='next')
def logout_view(request):
    messages.success(request, 'Logout sucedido')
    logout(request)
    return redirect(reverse('accounts:login'))
