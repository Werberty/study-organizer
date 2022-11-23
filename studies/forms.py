from django import forms

from .models import Study, Subject


class StudyForm(forms.ModelForm):
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


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = (
            'name',
            'contents',
            'color',
        )
        widgets = {
            'color': forms.Select(
                attrs={
                    'class': 'subject-color',
                    'type': 'color'
                }
            )
        }
