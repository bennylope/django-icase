import mock

from django.test import TestCase
from django.test.client import RequestFactory

from icase.views import icase_404_handler


class Test404View(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @mock.patch('icase.views.page_not_found')
    def test_404_error(self, page_not_found):
        """Ensure a normalized URL returns 404"""
        page_not_found.return_value = False
        request = self.factory.request()
        request.path = "/lowercase/"
        response = icase_404_handler(request)
        self.assertEqual(response, False)

    def test_redirect(self):
        request = self.factory.request()
        request.path = "/CamelCase/"
        response = icase_404_handler(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], "/camelcase/")
