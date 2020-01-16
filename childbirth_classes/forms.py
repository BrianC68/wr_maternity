from django import forms
from childbirth_classes.models import ChildbirthClassBooking


class ChildbirthClassBookingForm(forms.ModelForm):
    '''Form used to sign up for childbirth classes.'''

    class Meta:
        model = ChildbirthClassBooking
        exclude = ['paid']
        widgets = {'cb_class': forms.HiddenInput(), 'cost': forms.HiddenInput()}
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'partner_name': 'Partner Name',
            'postal_code': 'Postal Code',
        }
