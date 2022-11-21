from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import StudyForm, SubjectForm
from .models import Study, Subject


def studies(request):
    studies = Study.objects.all()
    subjects = Subject.objects.all()
    form_study = StudyForm()
    form_subject = SubjectForm()

    return render(request, 'studies/studies.html', context={
        'studies': studies,
        'subjects': subjects,
        'form_study': form_study,
        'form_subject': form_subject,
    })


def create_study(request):
    if not request.POST:
        raise Http404()

    form = StudyForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect(reverse('studies:studies'))


def create_subject(request):
    if not request.POST:
        raise Http404()

    form = SubjectForm(request.POST)

    if form.is_valid():
        form.save()

    return redirect(reverse('studies:studies'))


def subject(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'studies/subject.html', context={
        'subject': subject,
    })
