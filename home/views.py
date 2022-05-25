
from django.views.generic import  TemplateView, ListView
from roombook.models import RoomType
from reviews.models import Reviews
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import redirect, reverse

# Create your views here.


class HomeView(TemplateView): # happpy
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room_types'] = RoomType.objects.all()
        # only showcase reviews which are featured
        context['reviews'] = Reviews.objects.filter(featured= True)
        return context

class InfoView(TemplateView):# happy
    template_name = 'home/info.html'


class StaffView(ListView):
    template_name = 'home/staff.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        return Reviews.objects.filter(
            approved=False)

def approvereview(request,pk):
    user = request.user
    if user.is_staff:
        booking = get_object_or_404(Reviews,pk=pk)
        booking.approved = True
        booking.save()
        messages.warning(request, f'Review number { booking.id } has been approved')
        return redirect(reverse('home:staff'))
    else:
        messages.warning(request, 'Reviews may only be approved by staff members')
        return redirect(reverse('home:home'))
    