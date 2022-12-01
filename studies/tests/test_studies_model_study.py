from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_studies_base import StudiesBaseTest


class StudyModelsTest(StudiesBaseTest):
    def setUp(self) -> None:
        self.study = self.make_study()
        return super().setUp()

    @parameterized.expand([
        ('weekday', 255)
    ])
    def test_study_fields_max_legth(self, field, max_length):
        setattr(self.study, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.study.full_clean()
