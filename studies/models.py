from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Subject(models.Model):
    CHOICES = (
        ('blue', 'Azul'),
        ('orange', 'Laranja'),
        ('yellow', 'Amarelo'),
        ('red', 'Vermelho'),
        ('green', 'Verde'),
        ('pink', 'Rosa'),
        ('purple', 'Roxo'),
    )

    student = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=8, choices=CHOICES, default='azul')
    contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Study(models.Model):
    CHOICES = (
        ('Sunday', 'Domingo'),
        ('Monday', 'Segunda-feira'),
        ('Tuesday', 'Terça-feira'),
        ('Wednesday', 'Quarta-feira'),
        ('Thursday', 'Quinta-feira'),
        ('Friday', 'Sexta-feira'),
        ('Saturday', 'Sábado'),
    )

    weekday = models.CharField(max_length=9, choices=CHOICES)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name='studies')
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.weekday} {self.subject}'


class Content(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE,
        related_name='content_list'
    )

    def __str__(self) -> str:
        return self.name


class Historic(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    contents_studied = models.ManyToManyField(Content)
    date = models.DateTimeField(auto_now=True)
