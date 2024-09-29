from django.urls import reverse
from django.test import TestCase

class PyPiPackageViewTests(TestCase):
    
    def test_html_idlegame_contains_bboonstra(self):
        """
        Ensure the /html/idlegame page contains 'bboonstra' in the response.
        """
        response = self.client.get(reverse('get_html', args=['idlegame']))
        self.assertIn(b'Ben Boonstra', response.content)  # Check content directly

    def test_html_invalid_package_contains_not_valid_message(self):
        """
        Ensure the /html/_ page for an invalid package contains 'is not a valid PyPi package' in the response.
        """
        response = self.client.get(reverse('get_html', args=['_']))
        self.assertIn(b'is not a valid PyPi package', response.content)  # Check content directly

    def test_json_idlegame_contains_bboonstra(self):
        """
        Ensure the /json/idlegame JSON response contains 'bboonstra' in the 'html' field.
        """
        response = self.client.get(reverse('get_json', args=['idlegame']))
        self.assertIn(b'Ben Boonstra', response.content)  # Check content directly

    def test_json_invalid_package_contains_not_valid_message(self):
        """
        Ensure the /json/_ JSON response for an invalid package contains 'is not a valid PyPi package' in the 'html' field.
        """
        response = self.client.get(reverse('get_json', args=['_']))
        self.assertIn(b'is not a valid PyPi package', response.content)  # Check content directly
