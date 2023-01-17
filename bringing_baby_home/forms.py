from django import forms
from .models import BringingBabyHomeClassBooking


class BringingBabyHomeClassBookingForm(forms.ModelForm):
    '''Form used to sign up for classes.'''

    class Meta:
        model = BringingBabyHomeClassBooking
        exclude = ['paid']
        widgets = {'bbh_class': forms.HiddenInput(), 'cost': forms.HiddenInput()}
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'partner_name': 'Partner Name',
            'postal_code': 'Postal Code',
        }
