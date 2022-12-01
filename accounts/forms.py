from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='Usuário'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(),
        label='E-mail'
    )
    first_name = forms.CharField(
        label='Nome'
    )
    last_name = forms.CharField(
        label='Sobrenome'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha'
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(),
        label='Senha novamente'
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
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'span-2'
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data['password']
        password2 = cleaned_data['password2']

        if password1 == password2:
            raise ValidationError('Senhas diferentes!')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
