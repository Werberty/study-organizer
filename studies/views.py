from django.shortcuts import render

from .forms import StudyForm
from .models import Study, Subject


def home(request):
    studies = Study.objects.all()
    form = StudyForm()

    return render(request, 'studies/home.html', context={
        'studies': studies,
        'form': form,
    })


def subject(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'studies/subject.html', context={
        'subject': subject,
    })
