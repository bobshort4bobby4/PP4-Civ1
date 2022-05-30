
"""
forms used in the application
"""
from django import forms
from roombook.models import Booking
from reviews.models import Reviews


class AvailabilityForm(forms.Form):
    """
    form used in check availability
    """
    check_in = forms.DateField(required=True, widget=forms.DateTimeInput(
                                                    attrs={'type': 'date'}))
    check_out = forms.DateField(required=True, widget=forms.DateTimeInput(
                                                    attrs={'type': 'date'}))

    class Meta:
        fields = ['check_in', 'check_out']


class CancelConfirmForm(forms.Form):
    """
    form used in cancel a booking
    """
    model = Booking

    class Meta:
        fields = ['user', 'room_number', 'check_in', 'check_out']


class ExtendBookingForm(forms.Form):
    """
    form used to extend stay
    """

    new_check_out = forms.DateField(required=True, widget=forms.DateTimeInput(
                            attrs={'type': 'date'}), label=' New Check-Out')

    class Meta:
        fields = ['check_out']

    def __init__(self, oldcheck_out, *args, **kwargs):

        # call standard __init__
        super().__init__(*args, **kwargs)

        global old_check_out
        old_check_out = oldcheck_out

    def clean_new_check_out(self):
        """
        validate the new check out date
        """
        datum = self.cleaned_data.get('new_check_out')
        print(self.errors.as_data)

        if datum <= old_check_out:
            self.add_error('new_check_out', "dates are wrong")
        return datum
