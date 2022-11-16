from django.urls import path

from . import views

app_name = 'studies'

urlpatterns = [
    path('', views.home, name='home'),
    path('subject/<int:id>/', views.subject, name='subject'),
]
