from django.urls import path

from . import views

app_name = 'studies'

urlpatterns = [
    path('', views.studies, name='studies'),
    path('study/new/', views.create_study, name='create_study'),
    path('subject/new/', views.create_subject, name='create_subject'),
    path('study/delete/<int:id>/', views.delete_study, name='delete_study'),
    path(
        'subject/delete/<int:id>/', views.delete_subject, name='delete_subject'
    ),
    path('subject/<int:id>/', views.subject, name='subject'),
]
