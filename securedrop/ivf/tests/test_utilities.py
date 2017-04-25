from bs4 import BeautifulSoup
from unittest import mock

from django.test import TestCase

from ivf import utils


class VerificationUtilityTest(TestCase):
    def test_https_is_in_url(self):
        self.assertTrue(utils.validate_https('https://example.com'))

    def test_https_is_not_in_url(self):
        self.assertFalse(utils.validate_https('example.com'))

    def test_onion_link_is_in_href(self):
        test_html = "<a href='notavalidaddress.onion'>SecureDrop</a>"
        soup = BeautifulSoup(test_html, "lxml")
        self.assertFalse(utils.validate_onion_address_not_in_href(soup))

    def test_onion_link_is_not_in_href(self):
        test_html = "Go to notavalidaddress.onion and leak dem docs"
        soup = BeautifulSoup(test_html, "lxml")
        self.assertTrue(utils.validate_onion_address_not_in_href(soup))

    def test_url_does_not_have_subdomain(self):
        self.assertFalse(utils.validate_subdomain('https://example.com/securedrop'))

    def test_url_does_have_subdomain(self):
        self.assertTrue(utils.validate_subdomain('https://securedrop.example.com'))

    def test_server_header_software_present(self):
        page = mock.Mock()
        page.headers = {'Server': 'nginx'}
        self.assertFalse(utils.validate_server_software(page))

    def test_server_header_software_not_present(self):
        page = mock.Mock()
        page.headers = {'Server': ''}
        self.assertTrue(utils.validate_server_software(page))

    def test_server_header_version_not_present(self):
        page = mock.Mock()
        page.headers = {'Server': ''}
        self.assertTrue(utils.validate_server_version(page))

    def test_server_header_version_not_present(self):
        page = mock.Mock()
        page.headers = {'Server': '6.6.6'}
        self.assertFalse(utils.validate_server_version(page))
