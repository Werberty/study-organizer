from django.shortcuts import render

from .models import Study, Subject


def home(request):
    studies = Study.objects.all()

    return render(request, 'studies/home.html', context={
        'studies': studies
    })


def subject(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'studies/subject.html', context={
        'subject': subject,
    })
