"""
    Myaccount views
"""
from datetime import date
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import redirect, reverse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, View
from roombook.models import Booking
from forms.forms import CancelConfirmForm, ExtendBookingForm
from booking_code.check_extendability import check_extendability


@method_decorator(login_required, name='dispatch')
class ShowDetails(ListView):
    """
        A generic veiw to list all booking of that customer
    """
    template_name = "myaccount/myaccount.html"
    model = Booking
    context_object_name = 'mybookings'

    # override init method to make sure custom model manager is called
    # thus preventing out of date booking being shown on my account page

    def __init__(self, **kwargs):
        Booking.objects.all()
        super().__init__(**kwargs)

    # queryset is all bookings belonging to that customer order by date

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user, is_active=True).order_by('check_in')


@method_decorator(login_required, name='dispatch')
class CancelBooking(SuccessMessageMixin, DeleteView):
    """
     Generic view to delete booking with id of pk.

    """
    # set queryset to one booking selected by user, passed in kwargs
    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return Booking.objects.filter(
            pk=pk)

    # add message into delete method
    def delete(self, request, *args, **kwargs):
        bookid = self.kwargs.get('pk', None)
        bookid = get_object_or_404(Booking, pk=bookid)
        # check that the booking is owned by the logged in user
        user = self.request.user
        if bookid.user.username == user.username:
            messages.success(self.request, self.success_message)
            email = request.user.email
            send_mail(
                'Booking Cancelation',
                'Thank you.\nYour booking for the Flower Hotel.\n' +
                'Booking id ' + str(bookid.id) + '\n' +
                'Room Number ' + str(bookid.room_number) + '\n' +
                'Check in ' + str(bookid.check_in) + '\n' +
                'Check Out ' + str(bookid.check_out) + '\n' +
                'Has been canceled',
                'example.com',
                [email],
                fail_silently=False,
            )
            return super(CancelBooking, self).delete(request, *args, **kwargs)
        else:
            messages.warning(request, 'Sorry! This does not appear\
                                to be your booking please contact us for help')
            return redirect(reverse('myaccount:myaccount'))

    model = Booking
    template_name = "myaccount/cancel_booking.html"
    form_class = CancelConfirmForm
    success_url = reverse_lazy("home:home")
    success_message = "The booking has been canceled"

    # overriding get method to check the checkin date is not too close
    def get(self, request, *args, **kwargs):
        user = self.request.user
        bookid = self.kwargs.get('pk', None)
        booking = get_object_or_404(Booking, pk=bookid)
        # checkin to ensure user has the right to view this booking details
        if booking.user.username == user.username:
            today = date.today()
            checkin = booking.check_in
            # if checkin over 7 days away then cancel
            if (checkin - today).days >= 7:
                return render(request, self.template_name, {'booking': booking})
            # if checkin less than 7 days away then deny cancel request
            elif (checkin - today).days < 7:
                messages.warning(request, 'Sorry! Cancelation only\
                    possible if checkin date is more than 7 days away')
                return redirect(reverse('myaccount:myaccount'))
            # if checkin is past tense, deny cancellation request
            elif checkin < today:
                messages.warning(request, 'Sorry! Checkin date has passed')
                return redirect(reverse('myaccount:myaccount'))
            else:
                return redirect(reverse('myaccount:myaccount'))
        else:
            raise PermissionDenied()


@method_decorator(login_required, name='dispatch')
class ExtendBooking(View):
    """
    Class based view to handle stay extension request
    """

    template_name = 'myaccount/extend_booking.html'

    def get(self, request, **kwargs):

        # pass booking data into template
        bookid = self.kwargs.get('pk', None)
        bookid = get_object_or_404(Booking, pk=bookid)

        # pass old check-out date into form for validation
        form = ExtendBookingForm(bookid.check_out)
        context = {
            'bookid': bookid,
            'form': form
        }

        user = self.request.user
        # checking to ensure user has right to view this booking details
        if bookid.user.username == user.username:
            return render(request, self.template_name, context)
        else:
            raise PermissionDenied()

    def post(self, request, **kwargs):
        # pass booking data into template
        bookid = self.kwargs.get('pk', None)
        bookid = get_object_or_404(Booking, pk=bookid)

        user = self.request.user
        # check proper user
        if bookid.user.username == user.username:
            # pass old check-out date into form for validation and form data
            form = ExtendBookingForm(bookid.check_out, request.POST)

            # if new check-out date valid continue else
            #  display error alert and redirect
            if form.is_valid():
                data = form.cleaned_data
            else:
                messages.warning(request, 'Form not valid, New check-out date\
                                             must be after old check-out date')
                return redirect(reverse('myaccount:myaccount'))

            # if particlar room availabile extend booking,
            #  display thank you info and redirect to home
            if check_extendability(
                                    bookid.room_number,
                                    bookid.check_out,
                                    data['new_check_out']):
                bookid.check_out = data['new_check_out']
                bookid.save()
                messages.success(
                                request, f"Thank you for extending room { bookid.room_number } \
                                to { data['new_check_out'] }")
                email = request.user.email
                # confirmation email
                send_mail(
                    'Booking Extended',
                    'Thank you.\nYour booking for the Flower Hotel.\n' +
                    'Booking id ' + str(bookid.id) + '\n' +
                    'Room Number ' + str(bookid.room_number) + '\n' +
                    'Check in ' + str(bookid.check_in) + '\n' +
                    'Has been extended to ' + str(bookid.check_out),
                    'example.com',
                    [email],
                    fail_silently=False,
                )
                return redirect(reverse('home:home'))
            # display alert about room not available and redirect
            else:
                messages.warning(request, "Sorry that room is not available\
                                            for those dates, try another room")
                return redirect(reverse('home:home'))
        else:
            messages.warning(request, 'Sorry! This does not appear to be your\
                                        booking please contact us for help')
            return redirect(reverse('myaccount:myaccount'))
