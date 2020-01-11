from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(required=True, max_length=100)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': '500 Character Limit'}), max_length=500, label='Message')
