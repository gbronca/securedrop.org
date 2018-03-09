import re

from bs4 import BeautifulSoup

from django.test import TestCase

from wagtail.wagtailcore.models import Site

from common.models import DirectorySettings
from directory.tests.factories import DirectoryPageFactory
from landing_page_checker.tests.factories import (
    SecuredropPageFactory,
    ResultFactory,
)


class DirectorySettingsTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        site = Site.objects.get(is_default_site=True)
        self.directory_settings = DirectorySettings.for_site(site)
        self.directory = DirectoryPageFactory(parent=site.root_page)
        self.securedrop_page = SecuredropPageFactory(parent=self.directory)
        self.result = ResultFactory(securedrop=self.securedrop_page)

    def test_scan_disabled_hides_directory_scan_results(self):
        self.directory_settings.show_scan_results = False
        self.directory_settings.save()

        response = self.client.get(self.directory.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        grades = soup.find_all(class_='instance-table__grade-column')

        self.assertEqual(len(grades), 0)

    def test_scan_enabled_shows_directory_scan_results(self):
        self.directory_settings.show_scan_results = True
        self.directory_settings.save()

        response = self.client.get(self.directory.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        grades = soup.find_all(class_='instance-table__grade-column')

        self.assertEqual(len(grades), 1)

    def test_scan_disabled_hides_detail_scan_results(self):
        self.directory_settings.show_scan_results = False
        self.directory_settings.save()

        response = self.client.get(self.securedrop_page.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        grade = soup.find_all(class_='security_grade')
        result = soup.find_all(class_='scan-result')

        self.assertEqual(len(grade), 0)
        self.assertEqual(len(result), 0)

    def test_scan_enabled_shows_detail_scan_results(self):
        self.directory_settings.show_scan_results = True
        self.directory_settings.save()

        response = self.client.get(self.securedrop_page.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        grade = soup.find_all(class_='security_grade')
        result = soup.find_all(class_='scan-result')

        self.assertEqual(len(grade), 1)
        self.assertEqual(len(result), 1)

    def test_management_disabled_hides_call_to_action(self):
        self.directory_settings.allow_directory_management = False
        self.directory_settings.save()

        # We add a trailing `?` to account for the optional trailing slash
        scan_url_re = '{}{}?'.format(
            self.directory.url,
            self.directory.reverse_subpage('scan_view')
        )
        response = self.client.get(self.directory.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        scan_links = soup.find_all(href=re.compile(scan_url_re))

        self.assertEqual(len(scan_links), 0)

    def test_management_enabled_shows_call_to_action(self):
        self.directory_settings.allow_directory_management = True
        self.directory_settings.save()

        # We add a trailing `?` to account for the optional trailing slash
        scan_url_re = '{}{}?'.format(
            self.directory.url,
            self.directory.reverse_subpage('scan_view')
        )
        response = self.client.get(self.directory.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        scan_links = soup.find_all(href=re.compile(scan_url_re))

        self.assertTrue(len(scan_links) > 0)
