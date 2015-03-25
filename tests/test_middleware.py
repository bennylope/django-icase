from django.test import TestCase
from django.test.client import RequestFactory

from icase.middleware import LowerCased


class TestLowerCasedMiddleware(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_no_redirect(self):
        request = self.factory.request()
        request.path = "/lowercase/"
        response = LowerCased().handle_request(request)
        self.assertIsNone(response)

    def test_redirect(self):
        request = self.factory.request()
        request.path = "/LoEercase/"
        response = LowerCased().handle_request(request)
        self.assertIsNotNone(response)
