from django.contrib.auth.models import User
from django.test import TestCase

from studies.models import Study, Subject


class StudiesBaseTest(TestCase):
    def make_user(self,
                  username='User123',
                  password='Password',
                  email='email@email.com',
                  first_name='User',
                  last_name='Test'
                  ):

        return User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )

    def make_subject(self,
                     student=None,
                     name='Subject test',
                     color='azul',
                     contents='Content test'
                     ):
        if student is None:
            student = {}

        return Subject.objects.create(
            student=self.make_user(**student),
            name=name,
            color=color,
            contents=contents
        )

    def make_study(self,
                   weekday='Sunday',
                   subject=None,
                   start_time='6:00',
                   end_time='7:00'
                   ):
        if subject is None:
            subject = {}

        return Study.objects.create(
            weekday=weekday,
            subject=self.make_subject(**subject),
            start_time=start_time,
            end_time=end_time
        )

    def login_user(self, username='User123', password='Password'):
        return self.client.login(username=username, password=password)
