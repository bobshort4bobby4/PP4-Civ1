"""
Views for review app
"""

from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Reviews


class ReviewView(ListView):
    """
    displays all approved reviews
    paginates on 5 items
    """
    model = Reviews
    template_name = 'reviews/review.html'
    context_object_name = 'hotel_reviews'
    paginate_by = 5

    # display all review which are approved
    def get_queryset(self):
        return Reviews.objects.filter(
            approved=True)


class CreateReview(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    Handles the creation of a new review
    uses two mixin classes
    loginrequired and Successmessage
    """
    model = Reviews
    login_url = '/'
    template_name = 'reviews/create_review.html'
    fields = ['text']
    success_url = '/'
    permission_denied_message = 'Please login to leave a review.'
    success_message = 'Thank you for your feedback.\
                             Please allow 24 hours for activation on the site'

    # pre-populate the user field with the current logged in user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # setup messages for permission denied
    def handle_no_permission(self):
        messages.error(self.request, self.permission_denied_message)
        return super(CreateReview, self).handle_no_permission()
