from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
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
                    'class': 'colun-2'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'colun-2'
                }
            )
        }
