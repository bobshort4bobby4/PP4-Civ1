from django.shortcuts import render
from django.views.generic import ListView, DeleteView, View
from roombook.models import Booking
from django.contrib import messages
from django.shortcuts import redirect, reverse
from datetime import date
from django.shortcuts import get_object_or_404
from forms.forms import CancelConfirmForm, ExtendBookingForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from booking_code.check_extendability import check_extendability


class ShowDetails(ListView):# happy
    
    template_name = "myaccount/myaccount.html"
    model = Booking
    context_object_name = 'mybookings'

    def get_queryset(self):
        return Booking.objects.filter(
            user=self.request.user, is_active=True)
 

class CancelBooking(SuccessMessageMixin, DeleteView):# think im happy custom code has to go somewhere?
    # set queryset to one booking selected by user, passed in kwargs
    def get_queryset(self):
        pk = self.kwargs.get('pk', None)
        return Booking.objects.filter(
            pk=pk)
    # add message into delete method
    def delete(self, request, *args, **kwargs):
        bookid = type = self.kwargs.get('pk', None)
        bookid = get_object_or_404(Booking, pk=bookid)

        user=self.request.user
        if bookid.user.username == user.username:
            messages.success(self.request, self.success_message)
            return super(CancelBooking, self).delete(request, *args, **kwargs)
        else:
            messages.warning(request, 'Sorry! This does not appear to be your booking please contact us for help')
            return redirect(reverse('myaccount:myaccount'))


    model = Booking
    template_name= "myaccount/cancel_booking.html"
    form_class = CancelConfirmForm
    success_url = reverse_lazy("home:home")
    success_message  = "The booking has been canceled"
    
    # overriding get method to check the checkin date is not too close
    def get(self, request, *args, **kwargs):
        bookid = self.kwargs.get('pk', None)
        today = date.today()
        booking = get_object_or_404(Booking, pk=bookid)
        checkin = booking.check_in
        if (checkin - today).days >= 7:
            return render(request, self.template_name, {'booking':booking})
        elif (checkin - today).days < 7:
            messages.warning(request, 'Sorry! Cancelation only possible if checkin date is more than 7 days away')
            return redirect(reverse('myaccount:myaccount'))
        elif (checkin < today):
             messages.warning(request, 'Sorry! Checkin date has passed')
             return redirect(reverse('myaccount:myaccount'))
        else:
            return redirect(reverse('myaccount:myaccount'))



class ExtendBooking(View):# not happy with this one, working ok
    
    template_name = 'myaccount/extend_booking.html'
    

    def get(self, request, *args, **kwargs):

        # pass booking data into template
        bookid = self.kwargs.get('pk', None)
        bookid = get_object_or_404(Booking, pk=bookid)
    
        # pass old check-out date into form for validation
        form = ExtendBookingForm(bookid.check_out)
        context = {
            'bookid': bookid,
            'form': form
        }
        return render(request, self.template_name, context)
    


    def post(self, request, *args, **kwargs):
        # pass booking data into template
        bookid = type = self.kwargs.get('pk', None)
        bookid = get_object_or_404(Booking, pk=bookid)

        user=self.request.user
        if bookid.user.username == user.username:
            # pass old check-out date into form for validation and form data
            form = ExtendBookingForm( bookid.check_out, request.POST)

            # if new check-out date valid continue else display error alert and redirect
            if form.is_valid():
                data = form.cleaned_data
            else:
                messages.warning(request, 'Form not valid, New check-out date must be after old check-out date')
                return redirect( reverse('myaccount:myaccount'))

            # if particlar room availabile extend booking,
            #  display thank you info and redirect to home
            if check_extendability(bookid.room_number, bookid.check_out, data['new_check_out']):
                bookid.check_out =  data['new_check_out']
                bookid.save()
                messages.success(
                                request, f"Thank you for extending room { bookid.room_number } \
                                to { data['new_check_out'] }")
                return redirect(reverse('home:home'))
            # display alert about room not available and redirect
            else:
                messages.warning(request, "Sorry that room is not available for those dates, try another room")
                return redirect(reverse('home:home'))
        else:
            messages.warning(request, 'Sorry! This does not appear to be your booking please contact us for help') 
            return redirect( reverse('myaccount:myaccount'))
