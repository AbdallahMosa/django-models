from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.
class SnacksTitsing(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    def test_temp(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response,"home.html")
    def test_snack_list(self):
        url=reverse('snacks')
        print(url)
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 200)
    def test_temp_snack_list(self):
        response = self.client.get(reverse('snacks'))
        self.assertTemplateUsed(response,"snack_list.html")