from django.test import TestCase, Client
from django.test import tag
from django.urls import reverse
from django.contrib.auth.models import User
from reviews.models import Reviews


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

    def test_staffview_renders_correct_template(self):
        client = Client()
        response = self.client.get(reverse('home:staff'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/staff.html')

    def test_approve_review_is_working(self):
        user = User.objects.create_user(
            username = 'robert',
            password = '1234',
            email = "mail@mail.com",
            is_staff = True,

        )
        self.review = Reviews.objects.create(
            user = user,
            text = 'space',
            created_on = '01/01/2020',
            approved = False,
            featured = False,
        )
        pk =1
        response = self.client.get(reverse('home:approve', kwargs={'pk':1}))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse('home:home'))


    def test_approve_review_is_working_logged(self):
        user = User.objects.create_user(
        username = 'robert',
        password = '1234',
        email = "mail@mail.com",
        is_staff = True,

        )
        self.review = Reviews.objects.create(
            user = user,
            text = 'space',
            created_on = '01/01/2020',
            approved = False,
            featured = False,
        )
        pk =1
        self.client.login(username='robert', password='1234')
        response = self.client.get(reverse('home:approve', kwargs={'pk':1}))
        self.assertTemplateUsed('/staff/')