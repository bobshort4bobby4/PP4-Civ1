"""
tests for home app
"""

from django.test import TestCase
from django.test import tag
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import Reviews


@tag('views')
class TestHomeViews(TestCase):
    """
    tests for home app
    """

    def test_homeview_renders_correct_template(self):
        response = self.client.get(reverse('home:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_infoview_renders_correct_template(self):

        response = self.client.get(reverse('home:info'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/info.html')

    def test_staffview_renders_correct_template_nonstaff(self):
        response = self.client.get(reverse('home:staff'))
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, '403.html')

    def test_approve_review_is_working(self):
        user = User.objects.create_user(
            username='robert',
            password='1234',
            email="mail@mail.com",
            is_staff=True,

        )
        self.review = Reviews.objects.create(
            user=user,
            text='space',
            created_on='01/01/2020',
            approved=False,
            featured=False,
        )

        response = self.client.get(reverse('home:approve', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))

    def test_approve_review_is_working_logged(self):
        user = User.objects.create_user(
            username='robert',
            password='1234',
            email="mail@mail.com",
            is_staff=True,

            )
        self.review = Reviews.objects.create(
            user=user,
            text='space',
            created_on='01/01/2020',
            approved=False,
            featured=False,
        )

        self.client.login(username='robert', password='1234')
        self.assertTemplateUsed('/staff/')
