from django.test import TestCase
from django.urls import reverse


class StudiesURLsTest(TestCase):
    def test_studies_studies_urls_is_correct(self):
        url = reverse('studies:home')
        self.assertEqual(url, '/')

    def test_studies_create_study_urls_is_correct(self):
        url = reverse('studies:create_study')
        self.assertEqual(url, '/study/new/')

    def test_studies_create_subject_urls_is_correct(self):
        url = reverse('studies:create_subject')
        self.assertEqual(url, '/subject/new/')

    def test_studies_delete_study_urls_is_correct(self):
        url = reverse('studies:delete_study', kwargs={'id': 1})
        self.assertEqual(url, '/study/delete/1/')

    def test_studies_delete_subject_urls_is_correct(self):
        url = reverse('studies:delete_subject', kwargs={'id': 1})
        self.assertEqual(url, '/subject/delete/1/')
