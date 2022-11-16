from django.contrib import admin

from .models import Study, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    ...
