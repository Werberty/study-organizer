from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from utils.validators import email_is_valid, strong_password


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    username = forms.CharField(
        label='Usuário',
        error_messages={
            'required': 'Nome de usuário é obrigatório',
            'min_length': 'Use no mínimo 4 caracteres',
            'max_length': 'Use máximo 150 caracteres'
        },
        help_text=(
            'Obrigatório. Entre 4 e 150 caracteres. '
            'Letras, números e @/./+/-/_ apenas.'
        ),
        min_length=4, max_length=150
    )

    email = forms.CharField(
        label='E-mail',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'exemplo@email.com'
            }
        ),
        required=False
    )

    first_name = forms.CharField(
        label='Nome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex: José'
            }
        ),
        required=False
    )

    last_name = forms.CharField(
        label='Sobrenome',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ex: Beto'
            }
        ),
        required=False
    )

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Senha não pode ser vazia'
        },
        validators=[strong_password]
    )

    password2 = forms.CharField(
        label='Confirme a senha',
        widget=forms.PasswordInput(),
        error_messages={
            'required': 'Repita sua senha'
        }
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self._my_errors['password'].append('Senhas diferentes')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data["email"]
        email_valid = email_is_valid(email)
        print(email_valid)

        if not email_valid:
            self._my_errors['email'].append('E-mail inválido')

        return email


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Usuário',
        widget=forms.TextInput({
            'class': 'span-2',
            'placeholder': 'Digite seu usuário'
        })
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput({
            'class': 'span-2',
            'placeholder': 'Digite sua senha'
        })
    )
