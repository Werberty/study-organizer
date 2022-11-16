from django.test import TestCase
from django.urls import reverse


class StudiesURLsTest(TestCase):
    def test_studies_home_urls_is_correct(self):
        url = reverse('studies:home')
        self.assertEqual(url, '/')
