from django import forms

from .models import Study, Subject


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = (
            'weekday',
            'subject',
        )


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = (
            'name',
            'contents',
        )
