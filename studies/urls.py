from django.urls import path

from . import views

app_name = 'studies'

urlpatterns = [
    path('', views.home, name='home'),
    path('historic/', views.historic_view, name='historic'),
    path('study/new/', views.create_study, name='create_study'),
    path('subject/new/', views.create_subject, name='create_subject'),
    path('study/delete/<int:id>/', views.delete_study, name='delete_study'),
    path(
        'subject/delete/<int:id>/', views.delete_subject, name='delete_subject'
    ),
    path('subject/<int:id>/', views.subject, name='subject'),
    path(
        'subject/update/<int:id>/', views.subject_update, name='subject_update'
    ),
    path('weekday/<str:weekday>/', views.weekday, name='weekday'),
]
