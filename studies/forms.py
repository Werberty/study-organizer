from collections import defaultdict

from django import forms
from django.core.exceptions import ValidationError

from .models import Study, Subject


class StudyForm(forms.ModelForm):

    subject = forms.ModelChoiceField(
        queryset=None
    )

    class Meta:
        model = Study
        fields = (
            'weekday',
            'subject',
            'start_time',
            'end_time',
        )
        labels = {
            'weekday': 'Dia da semana',
            'subject': 'Assunto',
            'start_time': 'Hora de início',
            'end_time': 'Hora de término',
        }
        widgets = {
            'start_time': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'time',
                }
            ),
            'end_time': forms.TimeInput(
                format='%H:%M',
                attrs={
                    'type': 'time',
                }
            )
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        subjects = Subject.objects.filter(student=user)
        self.fields['subject'].queryset = subjects

        self._my_errors = defaultdict(list)

    def clean(self):
        cleaned_data = super().clean()

        start_time = cleaned_data.get('start_time', None)
        end_time = cleaned_data.get('end_time', None)

        if end_time is not None and start_time is None:
            self._my_errors['start_time'].append(
                'Horário de termino precisa de um início')

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super().clean()


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = (
            'name',
            'contents',
            'color',
        )
        labels = {
            'name': 'Nome',
            'contents': 'Conteudos',
            'color': 'Cor da tag'
        }
        widgets = {
            'color': forms.Select(
                attrs={
                    'class': 'subject-color',
                    'type': 'color'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nome da matéria'
                }
            )
        }
