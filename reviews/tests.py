from django.test import TestCase
from django.test import tag
from django.urls import reverse
from .models import Reviews
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from datetime import date
from django.contrib.admin.sites import AdminSite
from .admin import ReviewsAdmin


@tag('views')
class TestReviewView(TestCase):

        def test_list_review_uses_correct_template(self):
                today = date.today()

                test_user = User.objects.create_user(
                        username='testuser3', password='testpw1'
                        )
                review = Reviews.objects.create(user= test_user,
                                                text='first review',
                                                created_on=today,
                                                approved=False,
                                                        featured=False
                                                        )
                response = self.client.get(reverse('reviews:reviews'))
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, 'reviews/review.html')

        def test_logged0ut_user_cannot_submit_review(self):
                self.client.logout()

                response = self.client.get(reverse('reviews:reviews'))
                reviews= Reviews.objects.all()
                self.assertEqual(len(reviews), 0)



@tag('models')
class TestReiewsModels(TestCase):

    
        def test_review_string_method_returns_correct_output(self):
                today = date.today()

                test_user = User.objects.create_user(
                        username='testuser3', password='testpw1'
                        )
                review = Reviews.objects.create(user= test_user,
                                                text='first review',
                                                created_on=today,
                                                approved=False,
                                                featured=False
                                                )
        
                self.assertEqual(str(review.user.username), 'testuser3')
                self.assertTrue(isinstance(review, Reviews))
        



@tag('admin')
class TestAdminSite(TestCase):

        def test_set_approved_to_true(self):
                today = date.today()
                test_user = User.objects.create_user(
                        username='testuser3', password='testpw1'
                        )

                review = Reviews.objects.create(user= test_user,
                                                text='first review',
                                                created_on=today,
                                                approved=False,
                                                featured=False
                                                        )
        
                # instance of admin 
                self.reviewsadmin = ReviewsAdmin(model=Reviews, admin_site=AdminSite())

                response = self.reviewsadmin.set_approved_to_true(request=review, queryset=Reviews.objects.all())
                review = get_object_or_404(Reviews, pk=1)
                
                self.assertEqual(review.approved, True)


        def test_set_is_featured_to_true(self):
                today = date.today()
                test_user = User.objects.create_user(
                        username='testuser3', password='testpw1'
                        )

                review = Reviews.objects.create(user=test_user,
                                                        text='first review',
                                                        created_on=today,
                                                        approved=False,
                                                        featured=False
                                                        )
                
                # instance of admin 
                self.reviewsadmin = ReviewsAdmin(model=Reviews, admin_site=AdminSite())

                response = self.reviewsadmin.set_featured_to_true(request=review, queryset=Reviews.objects.all())
                review = get_object_or_404(Reviews, pk=1)
                
                self.assertEqual(review.featured, True)


        def test_set_all_attributes_to_true(self):
                today = date.today()
                test_user = User.objects.create_user(
                        username='testuser3', password='testpw1'
                        )

                review = Reviews.objects.create(user= test_user,
                                                        text='first review',
                                                        created_on=today,
                                                        approved=False,
                                                        featured=False
                                                        )
                
                # instance of admin 
                self.reviewsadmin = ReviewsAdmin(model=Reviews, admin_site=AdminSite())

                response = self.reviewsadmin.set_all_attributes_to_true(request=review, queryset=Reviews.objects.all())
                review = get_object_or_404(Reviews, pk=1)
                
                self.assertEqual(review.featured, True)
                self.assertEqual(review.approved, True)


