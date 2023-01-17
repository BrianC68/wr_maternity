from django import forms
from .models import MakingMarriageWorkClassBooking


class MakingMarriageWorkClassBookingForm(forms.ModelForm):
    '''Form used to sign up for classes.'''

    class Meta:
        model = MakingMarriageWorkClassBooking
        # Exclude paid field from form
        exclude = ['paid']
        # Override these fields as hidden fields, their values are filled after the form is rendered
        widgets = {'mmw_class': forms.HiddenInput(), 'cost': forms.HiddenInput()}
        # Override the label tag text
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'postal_code': 'Postal Code',
        }
