from django.test import TestCase

from studies.models import Study, Subject


class StudiesBaseTest(TestCase):
    def make_subject(self,
                     name='Subject test',
                     color='azul',
                     contents='Content test'
                     ):
        return Subject.objects.create(
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
