from django.contrib import admin

from .models import Content, Historic, Study, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ...


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    ...


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    ...


@admin.register(Historic)
class HistoricAdmin(admin.ModelAdmin):
    list_display = ('study', 'date')
