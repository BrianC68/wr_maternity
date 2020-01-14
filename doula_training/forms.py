from django import forms
from doula_training.models import DoulaWorkshopBooking


class DoulaWorkshopBookingForm(forms.ModelForm):
    '''Form used to sign up for doula training workshops.'''

    class Meta:
        model = DoulaWorkshopBooking
        # Exclude paid field from form
        exclude = ['paid']
        # Override these fields as hidden fields, their values are filled after the form is rendered
        widgets = {'workshop': forms.HiddenInput(), 'location': forms.HiddenInput(), 'cost': forms.HiddenInput()}
        # Override the label tag text
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'postal_code': 'Postal Code',
        }
