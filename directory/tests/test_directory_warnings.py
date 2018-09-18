from django.test import Client, TestCase
from wagtail.wagtailcore.models import Site

from directory.tests.factories import (
    DirectoryEntryFactory,
    DirectoryPageFactory,
    ScanResultFactory,
)


class DirectoryNoWarningTest(TestCase):
    def setUp(self):
        site = Site.objects.get()
        self.entry = DirectoryEntryFactory(
            parent=DirectoryPageFactory(parent=site.root_page)
        )
        self.result = ScanResultFactory(
            securedrop=self.entry,
            landing_page_url=self.entry.landing_page_url,
            no_failures=True,
        )
        self.result.save()
        self.entry.save()

        self.client = Client()

    def test_thing(self):
        response = self.client.get(self.entry.url, {'warnings': '1'})
        self.assertEqual(response.status_code, 200)


class DirectoryModerateWarningTest(TestCase):
    def setUp(self):
        site = Site.objects.get()
        self.entry = DirectoryEntryFactory(
            parent=DirectoryPageFactory(parent=site.root_page)
        )
        self.result = ScanResultFactory(
            securedrop=self.entry,
            landing_page_url=self.entry.landing_page_url,
            moderate_warning=True,
        )
        self.result.save()
        self.entry.save()

        self.client = Client()

    def test_warning_presence(self):
        """warning should be displayed if warnings flag in request"""
        response = self.client.get(self.entry.url, {'warnings': '1'})
        self.assertContains(
            response,
            'We recommend only visiting this SecureDrop landing page <a href="https://www.torproject.org/download/download-easy.html.en">using the Tor browser</a>.',
            status_code=200,
        )

    def test_warning_test_absence(self):
        """warning should not be displayed if warnings flag not in request"""
        response = self.client.get(self.entry.url)

        self.assertNotContains(
            response,
            'We recommend only visiting this SecureDrop landing page <a href="https://www.torproject.org/download/download-easy.html.en">using the Tor browser</a>.',
            status_code=200,
        )

    def test_warning_message_suppressed_if_page_ignores_all_triggered_warnings(self):
        self.entry.warnings_ignored = ['safe_onion_address']
        self.entry.save()

        response = self.client.get(self.entry.url, {'warnings': '1'})

        self.assertNotContains(
            response,
            'We recommend only visiting this SecureDrop landing page <a href="https://www.torproject.org/download/download-easy.html.en">using the Tor browser</a>.',
            status_code=200,
        )

    def test_single_warning_message_suppressed_if_page_ignores_that_warning(self):
        self.result.subdomain = True
        self.result.save()
        self.entry.warnings_ignored = ['safe_onion_address']
        self.entry.save()

        response = self.client.get(self.entry.url, {'warnings': '1'})
        self.assertContains(
            response,
            'is hosted on a subdomain',
            status_code=200,
        )

        self.assertNotContains(
            response,
            'contains clickable onion addresses',
            status_code=200,
        )


class DirectorySevereWarningTest(TestCase):
    def setUp(self):
        site = Site.objects.get()
        self.entry = DirectoryEntryFactory(
            parent=DirectoryPageFactory(parent=site.root_page)
        )
        self.result = ScanResultFactory(
            securedrop=self.entry,
            landing_page_url=self.entry.landing_page_url,
            severe_warning=True,
        )
        self.result.save()
        self.entry.save()

        self.client = Client()

    def test_warning_presence(self):
        """warning should be displayed if warnings flag in request"""
        response = self.client.get(self.entry.url, {'warnings': '1'})
        self.assertContains(
            response,
            'We strongly advise you to only visit this landing page <a href="https://www.torproject.org/">using the Tor browser</a>, with the <a href="https://safetydocs.example/">safety slider set to "safest"</a>.',
            status_code=200,
        )

    def test_warning_test_absence(self):
        """warning should not be displayed if warnings flag not in request"""
        response = self.client.get(self.entry.url)
        self.assertNotContains(
            response,
            'We strongly advise you to only visit this landing page <a href="https://www.torproject.org/">using the Tor browser</a>, with the <a href="https://safetydocs.example/">safety slider set to "safest"</a>.',
            status_code=200,
        )

    def test_warning_message_suppressed_if_page_ignores_all_triggered_warnings(self):
        self.entry.warnings_ignored = ['no_cookies']
        self.entry.save()
        self.entry.refresh_from_db()
        response = self.client.get(self.entry.url, {'warnings': '1'})
        self.assertNotContains(
            response,
            'We strongly advise you to only visit this landing page <a href="https://www.torproject.org/">using the Tor browser</a>, with the <a href="https://safetydocs.example/">safety slider set to "safest"</a>.',
            status_code=200,
        )

    def test_single_warning_message_suppressed_if_page_ignores_that_warning(self):
        self.result.no_analytics = False
        self.result.save()
        self.entry.warnings_ignored = ['no_analytics']
        self.entry.save()

        response = self.client.get(self.entry.url, {'warnings': '1'})
        self.assertContains(
            response,
            'uses cookies',
            status_code=200,
        )

        self.assertNotContains(
            response,
            'uses analytics',
            status_code=200,
        )