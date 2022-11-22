from django import forms

from .models import Study, Subject


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = (
            'weekday',
            'subject',
        )
        labels = {
            'weekday': 'Dia da semana',
            'subject': 'Assunto',
        }


class SubjectForm(forms.ModelForm):
    # color = forms.CharField(

    # )

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
