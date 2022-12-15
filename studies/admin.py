from django.contrib import admin

from .models import Content, Study, Subject, historic


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    ...


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    ...


@admin.register(historic)
class HistoricAdmin(admin.ModelAdmin):
    ...
