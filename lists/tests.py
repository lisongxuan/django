from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

from django.http import HttpRequest
class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')
    '''def test_root_url_resolve_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    def test_home_page_returns_correct_html(self):
        response=self.client.get('/')
        
        html=response.content.decode('utf8')
        expected_html = render_to_string('home.html')
        self.assertEqual(html,expected_html)
'''
