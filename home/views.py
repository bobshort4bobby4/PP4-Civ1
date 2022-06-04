"""
home app views
"""
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, ListView
from roombook.models import RoomType
from reviews.models import Reviews
# from decorators import role_required
from django.core.exceptions import PermissionDenied

# Create your views here.


class HomeView(TemplateView):
    """
    Generic class used to display home page
    get_context_data is overridden to
    include roomtypes and only reviews
    which have been approved
    """
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.all()
        # only showcase reviews which are featured
        context['reviews'] = Reviews.objects.filter(featured=True)
        return context


class InfoView(TemplateView):
    """
    Generic class used to display information page
    """
    template_name = 'home/info.html'


class StaffView(ListView):
    """
    Generic View used to display staff
    page, queryset is all unapproved
    reviews
    """
    template_name = 'home/staff.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        user = self.request.user
        # check proper user
        if user.is_staff:
            return Reviews.objects.filter(
                approved=False)
        else:
            raise PermissionDenied


def approvereview(request, pk):
    """
    function used to approve reviews
    only available to staff

    Parameters:
    pk: int

    """
    user = request.user
    if user.is_staff:
        booking = get_object_or_404(Reviews, pk=pk)
        booking.approved = True
        booking.save()
        messages.warning(
            request, f'Review number { booking.id } has been approved')
        return redirect(reverse('home:staff'))
    else:
        messages.warning(
            request, 'Reviews may only be approved by staff members')
        return redirect(reverse('home:home'))
