from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import MakingMarriageWorkClass, MakingMarriageWorkClassBooking
from .forms import MakingMarriageWorkClassBookingForm
from paypal.standard.forms import PayPalPaymentsForm
from wr_maternity import settings
from datetime import date


class MakingMarriageWorkClasses(ListView):

    template_name = "marriage_classes.html"
    model = MakingMarriageWorkClass
    context_object_name = 'classes'
    todays_date = date.isoformat(date.today())

    def get_queryset(self):
        queryset = super().get_queryset().order_by('class_date').filter(is_active=True, class_date__gte=self.todays_date)
        return queryset


class CreateMakingMarriageWorkClassBooking(CreateView):
    '''Page that displays MMW class booking form.'''

    model = MakingMarriageWorkClassBooking
    form_class = MakingMarriageWorkClassBookingForm
    template_name = 'mmw_booking_form.html'

    def get_context_data(self, **kwargs):
        # Get class context for use on the page
        context = super().get_context_data(**kwargs)
        class_detail = MakingMarriageWorkClass.objects.filter(pk=self.kwargs['pk'])
        context['class_detail'] = class_detail
        # If there are already 10 bookings, return message that the workshop is full
        attendees = MakingMarriageWorkClassBooking.objects.filter(mmw_class=self.kwargs['pk']).count()
        if attendees >= 10:
            context['message'] = 'Sorry, this class is full! Please choose another class to attend.'
        return context
        

    def get_initial(self, **kwargs):
        # Get primary key to use in the form
        initial = super().get_initial(**kwargs)
        cost = MakingMarriageWorkClass.objects.get(pk=self.kwargs['pk']).price
        if self.request.method == 'GET':
            initial['mmw_class'] = self.kwargs['pk']
            initial['cost'] = cost
            return initial
        else:
            return initial

    def get_success_url(self):
        return reverse('making_marriage_work:success', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        # If the form is valid, email the workshop attendee and the owner
        name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
        address = form.cleaned_data['address']
        city = form.cleaned_data['city']
        state = form.cleaned_data['state']
        postal_code = form.cleaned_data['postal_code']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        mmw_class = form.cleaned_data['mmw_class']
        message = f"The following person has signed up for a class.\n\n \
        {name}\n \
        {email}\n \
        {phone}\n \
        Class: {mmw_class.title}\n \
        Starting: {mmw_class.class_date}\n\n \
        Login in for details: https://www.well-roundedmaternity.com/admin/making_marriage_work/makingmarriageworkclassbooking/"

        message2 = f"Thank you for signing up for a class with Well-Rounded Family Services! Details are below.\n\n \
        {name}\n \
        {address}\n \
        {city}, {state} {postal_code}\n \
        {email}\n \
        {phone}\n \
        Class: {mmw_class.title}\n \
        Starting: {mmw_class.class_date}\n \
        Location: Remote via Zoom\n\n"
        message2 += "You will receive a reminder email two weeks prior to class with any further details and instructions.\n\n"
        message2 += "If you have any questions, please contact Coral Slavin @ 262-893-9945. We look forward to seeing you in class!\n\n\nWell-Rounded Family Services"

        to_email = [User.objects.get(id=2).email]
        subject = 'Making Marriage Work Booking'
        from_email = 'coral.slavin@gmail.com'
        try:
            send_mail(subject, message, from_email, to_email)
            send_mail(subject, message2, from_email, [email])
        except BadHeaderError:
            pass

        return super().form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class MakingMarriageWorkClassBookingSuccess(TemplateView):
    '''Redirect to template_name after successfully registering for class.'''

    template_name = 'mmw_booking_success.html'

    def get_context_data(self, **kwargs):
        # Get MMW class booking details to display on page
        context = super().get_context_data(**kwargs)
        booking = MakingMarriageWorkClassBooking.objects.get(id=kwargs['pk'])
        context['booking_detail'] = booking

        # Dictionary used to populate the PayPal IPN form.
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': booking.cost,
            'item_name': booking.mmw_class.title,
            'invoice': f"dw{str(booking.pk)}",
            'currency_code': 'USD',
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return': self.request.build_absolute_uri(reverse('payment-success')),
            'cancel_return': self.request.build_absolute_uri(reverse('making_marriage_work:success', kwargs={'pk': booking.pk})),
            'custom': booking.pk,
        }

        # Paypal payment form instance.
        form = PayPalPaymentsForm(initial=paypal_dict)
        context['form'] = form

        context['request'] = self.request

        return context
