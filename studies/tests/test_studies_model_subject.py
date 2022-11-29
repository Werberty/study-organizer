from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_studies_base import StudiesBaseTest


class SubjectModelsTest(StudiesBaseTest):
    def setUp(self) -> None:
        self.subject = self.make_subject()
        return super().setUp()

    @parameterized.expand([
        ('name', 255),
        ('color', 8)
    ])
    def test_subject_fields_max_legth(self, field, max_length):
        setattr(self.subject, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.subject.full_clean()
