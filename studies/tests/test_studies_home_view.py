from django.urls import resolve, reverse

from studies.views import home

from .test_studies_base import StudiesBaseTest


class StudiesHomeViewsTest(StudiesBaseTest):

    def test_studies_home_view_function_is_correct(self):
        view = resolve(reverse('studies:home'))
        self.assertIs(view.func, home)

    def test_studies_home_view_returns_status_code_200(self):
        self.make_user()
        self.login_user()

        response = self.client.get(reverse('studies:home'))
        self.assertEqual(response.status_code, 200)

    def test_studies_home_view_loads_correct_template(self):
        self.make_user()
        self.login_user()

        response = self.client.get(reverse('studies:home'))
        self.assertTemplateUsed(response, 'studies/pages/studies.html')

    def test_studies_home_templates_loads_studies(self):
        self.make_study(subject={'name': 'Matemática'})
        self.login_user()

        response = self.client.get(reverse('studies:home'))
        content = response.content.decode('utf-8')
        response_context_studies = response.context['studies']

        self.assertIn('Matemática', content)
        self.assertEqual(len(response_context_studies), 1)

    def test_studies_home_template_dont_loads_subjects_not_exist(self):
        self.make_user()
        self.login_user()

        response = self.client.get(reverse('studies:home'))

        self.assertIn(
            'Nenhum assunto encontrado. '
            'Adicione um novo assunto para '
            'começar a organizar seus estudos.',
            response.content.decode('utf-8')
        )
