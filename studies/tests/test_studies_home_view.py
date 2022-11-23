from django.test import TestCase
from django.urls import resolve, reverse

from studies.views import home


class StudiesHomeViewsTest(TestCase):
    def test_studies_home_view_function_is_correct(self):
        view = resolve(reverse('studies:home'))
        self.assertIs(view.func, home)

    def test_studies_home_view_returns_status_code_200(self):
        response = self.client.get(reverse('studies:home'))
        self.assertEqual(response.status_code, 200)

    def test_studies_home_view_loads_correct_template(self):
        response = self.client.get(reverse('studies:home'))
        self.assertTemplateUsed(response, 'studies/pages/studies.html')
