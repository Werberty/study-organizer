from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
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
        labels = {
            'username': 'Usuário',
            'email': 'E-mail',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'password': 'Senha',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'span-2'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'autocomplete': 'off'
                }
            )
        }

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data['password']
        password2 = cleaned_data['password2']

        if password1 != password2:
            raise ValidationError('Senhas diferentes!')

        return cleaned_data


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput({
            'class': 'span-2'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput({
            'class': 'span-2'
        })
    )
