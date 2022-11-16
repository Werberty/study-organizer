from django.shortcuts import render

from .models import Study


def home(request):
    studies = Study.objects.all()

    return render(request, 'studies/home.html', context={
        'studies': studies
    })
