from collections import defaultdict

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Confirme a senha'
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
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': 'Senha',
        }
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Bento123'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ex: José'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Ex: Bento'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'exemplo@email.com'
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise ValidationError({
                'password': ValidationError(
                    'Senhas diferentes', code='invalid'
                )
            })

        return cleaned_data


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
