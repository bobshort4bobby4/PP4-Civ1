from django.test import TestCase, Client
from django.test import tag
from django.urls import reverse

@tag('views')
class TestHomeViews(TestCase):

    def test_homeview_renders_correct_template(self):
        client = Client()
        response = self.client.get(reverse('home:home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_infoview_renders_correct_template(self):
        client = Client()
        response = self.client.get(reverse('home:info'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/info.html')

    def test_contactview_renders_correct_template(self):
        client = Client()
        response = self.client.get(reverse('home:contact'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')
