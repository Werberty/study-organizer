from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from utils.make_month import list_days_month

from .forms import StudyForm, SubjectForm
from .models import Historic, Study, Subject


@login_required(login_url='accounts:login', redirect_field_name='next')
def home(request):
    studies = Study.objects.filter(
        subject__student=request.user).order_by('start_time')
    subjects = Subject.objects.filter(student=request.user)

    studies_form_data = request.session.get('studies_form_data') or None
    subject_form_data = request.session.get('subject_form_data') or None

    form_study = StudyForm(request.user, studies_form_data)
    form_subject = SubjectForm(subject_form_data)

    return render(request, 'studies/pages/studies.html', context={
        'studies': studies,
        'subjects': subjects,
        'form_study': form_study,
        'form_subject': form_subject,
    })


@login_required(login_url='accounts:login', redirect_field_name='next')
def create_study(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['studies_form_data'] = POST
    form = StudyForm(request.user, POST)

    if form.is_valid():
        form.save()
        del (request.session['studies_form_data'])
        messages.success(request, 'Estudo programado')
    else:
        messages.error(request, 'Erro no formulário')

    return redirect(reverse('studies:home'))


@login_required(login_url='accounts:login', redirect_field_name='next')
def create_subject(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['subject_form_data'] = POST
    form = SubjectForm(request.POST)

    if form.is_valid():
        form_subject = form.save(commit=False)
        form_subject.student = request.user
        form_subject.save()

        del (request.session['subject_form_data'])
        messages.success(request, 'Assunto adicionado')
    else:
        messages.error(request, 'Erro no formulário')

    return redirect(reverse('studies:home'))


@login_required(login_url='accounts:login', redirect_field_name='next')
def delete_study(request, id):
    study = get_object_or_404(Study, subject__student=request.user, pk=id)

    study.delete()
    messages.warning(request, 'Estudo deletado')

    return redirect(reverse('studies:home'))


@login_required(login_url='accounts:login', redirect_field_name='next')
def delete_subject(request, id):
    subject = get_object_or_404(Subject, student=request.user, pk=id)

    subject.delete()
    messages.warning(request, 'Assunto deletado')

    return redirect(reverse('studies:home'))


@login_required(login_url='accounts:login', redirect_field_name='next')
def subject(request, id):
    subject = get_object_or_404(Subject, student=request.user, pk=id)
    form = SubjectForm(instance=subject)

    return render(request, 'studies/pages/subject.html', context={
        'subject': subject,
        'form': form
    })


def subject_update(request, id):
    if not request.POST:
        raise Http404()

    subject = get_object_or_404(Subject, student=request.user, pk=id)
    form = SubjectForm(request.POST, instance=subject)

    if form.is_valid():
        form.save()
        messages.success(request, 'Assunto editado')
    else:
        messages.error(request, 'Erro ao editar')

    return redirect(reverse('studies:subject', kwargs={'id': subject.id}))


@login_required(login_url='accounts:login', redirect_field_name='next')
def weekday(request, weekday):
    studies = Study.objects.filter(
        subject__student=request.user, weekday=weekday).order_by('start_time')
    subjects = Subject.objects.filter(student=request.user)

    return render(request, 'studies/pages/weekday.html', context={
        'studies': studies,
        'weekday': weekday,
        'subjects': subjects
    })


def historic_view(request):
    historics = Historic.objects.all()

    month = list_days_month()
    return render(request, 'studies/pages/historic.html', context={
        'month': month,
        'historics': historics
    })
