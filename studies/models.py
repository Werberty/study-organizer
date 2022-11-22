from django.db import models


class Subject(models.Model):
    CHOICES = (
        ('azul', 'azul'),
        ('verde', 'verde'),
        ('vermelho', 'vermelho'),
        ('amarelo', 'amarelo'),
    )

    name = models.CharField(max_length=255)
    color = models.CharField(max_length=8, choices=CHOICES, default='azul')
    contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Study(models.Model):
    CHOICES = (
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    )

    weekday = models.CharField(max_length=9, choices=CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.weekday} {self.subject}'
