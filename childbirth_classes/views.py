from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, TemplateView
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import ChildbirthClass, ChildbirthClassBooking
from .forms import ChildbirthClassBookingForm
from locations.models import Location
from paypal.standard.forms import PayPalPaymentsForm
from wr_maternity import settings
from datetime import date


class ChildbirthClassIndex(ListView):
    '''Page that displays childbirth class descriptions and booking dates.'''

    template_name = 'childbirth_classes.html'
    model = ChildbirthClass
    context_object_name = 'classes'
    todays_date = date.today()

    def get_queryset(self):
        # Separate comprehensive and condensed in to different query sets
        queryset = {'comp_classes': super().get_queryset().filter(class_type='COMP', is_active=True, start_date__gte=self.todays_date).order_by('start_date'),
                    'cond_classes': super().get_queryset().filter(class_type='COND', is_active=True, start_date__gte=self.todays_date).order_by('start_date')}
        return queryset


class CreateChildbirthClassBooking(CreateView):
    '''Page that displays childbirth class booking form.'''

    template_name = 'childbirth_classes_booking_form.html'
    model = ChildbirthClassBooking
    form_class = ChildbirthClassBookingForm

    def get_context_data(self, **kwargs):
        # Get childbirth class context for use on the page.
        context = super().get_context_data(**kwargs)
        class_detail = ChildbirthClass.objects.filter(pk=self.kwargs['pk'])
        context['class_detail'] = class_detail
        # If there are already 10 bookings, return message that the class is full.
        attendees = ChildbirthClassBooking.objects.filter(cb_class=self.kwargs['pk']).count()
        if attendees >= 10:
            context['message'] = 'Sorry, this class is full! Please choose another class to attend.'
        return context

    def get_initial(self, **kwargs):
        # Get childbirth class details to use as values in the form.
        initial = super().get_initial(**kwargs)
        if self.request.method == 'GET':
            initial['cb_class'] = self.kwargs['pk']
            cost = ChildbirthClass.objects.filter(pk=self.kwargs['pk']).values_list('price', flat=True)
            initial['cost'] = cost[0]
            return initial
        else:
            return initial

    def get_success_url(self):
        return reverse('childbirth_classes:success', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        # If the form is valid, email the class attendee and the owner.
        name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        cb_class = form.cleaned_data['cb_class']
        message = f"The following person has signed up for a class.\n\n \
        {name}\n \
        {email}\n \
        {phone}\n \
        Class: {cb_class.title}\n \
        Starting: {cb_class.start_date}\n\n"
        message += "Login in for details: https://www.well-roundedmaternity.com/admin/childbirth_classes/childbirthclassbooking/"

        # {cb_class.location.location_name}\n \
        # {cb_class.location.location_address}\n \
        # {cb_class.location.location_city}, {cb_class.location.location_state} {cb_class.location.location_zip}\n\n"
        message2 = f"Thank you for signing up for a class with Well-Rounded Maternity! Details are below.\n\n \
        {name}\n \
        {email}\n \
        {phone}\n \
        Class: {cb_class.title}\n \
        Starting: {cb_class.start_date}\n \
        Ending: {cb_class.end_date}\n \
        Time: {cb_class.start_time.strftime('%I:%M %p')} to {cb_class.end_time.strftime('%I:%M %p')}\n \
        Location: Remote via Zoom\n\n"
        
        message2 += "You will receive a reminder email two weeks prior to class with further details and instructions.\n\n"
        message2 += "If you have any questions, please contact Coral Slavin @ 262-893-9945. We look forward to seeing you in class!\n\n\nWell-Rounded Maternity"
        
        to_email = [User.objects.get(id=2).email]
        subject = 'Childbirth Class Booking'
        from_email = 'info@well-roundedmaternity.com'
        try:
            send_mail(subject, message, from_email, to_email)
            send_mail(subject, message2, from_email, [email])
        except BadHeaderError:
            pass

        return super().form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class ChildbirthClassBookingSuccess(TemplateView):
    '''Redirect to template_name after successfully registering for childbirth class.'''

    template_name = 'childbirth_classes_booking_success.html'

    def get_context_data(self, **kwargs):
        # Get childbirth class booking details to display on page.
        context = super().get_context_data(**kwargs)
        booking = ChildbirthClassBooking.objects.get(id=kwargs['pk'])
        context['booking_detail'] = booking

        # Dictionary used to populate the PayPal IPN form.
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': booking.cost,
            'item_name': booking.cb_class.title,
            'invoice': f"cb{str(booking.pk)}",
            'currency_code': 'USD',
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return': self.request.build_absolute_uri(reverse('payment-success')),
            'cancel_return': self.request.build_absolute_uri(reverse('childbirth_classes:success', kwargs={'pk': booking.pk})),
            'custom': booking.id,
        }

        # Paypal payment form instance.
        form = PayPalPaymentsForm(initial=paypal_dict)
        context['form'] = form
        context['request'] = self.request
        return context
