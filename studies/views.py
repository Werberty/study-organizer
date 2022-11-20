from django.shortcuts import render

from .forms import StudyForm, SubjectForm
from .models import Study, Subject


def home(request):
    studies = Study.objects.all()
    form_study = StudyForm()
    form_subject = SubjectForm()

    return render(request, 'studies/home.html', context={
        'studies': studies,
        'form_study': form_study,
        'form_subject': form_subject,
    })


def subject(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'studies/subject.html', context={
        'subject': subject,
    })
