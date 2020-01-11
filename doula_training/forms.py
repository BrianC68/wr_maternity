from django import forms
from doula_training.models import DoulaWorkshopBooking


class DoulaWorkshopBookingForm(forms.ModelForm):
    '''Form used to sign up for doula training workshops.'''

    class Meta:
        model = DoulaWorkshopBooking
        exclude = ['paid']
        widgets = {'workshop': forms.HiddenInput(), 'location': forms.HiddenInput(), 'cost': forms.HiddenInput()}
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'postal_code': 'Postal Code',
        }
