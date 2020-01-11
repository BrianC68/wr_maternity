from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import DoulaWorkshop, DoulaWorkshopBooking
from .forms import DoulaWorkshopBookingForm
from paypal.standard.forms import PayPalPaymentsForm
from wr_maternity import settings


class DoulaTrainingIndex(ListView):
    '''Index view for Doula Training page.'''

    template_name = 'doula_training.html'
    model = DoulaWorkshop

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_active=True).order_by('start_date')
        return queryset


class CreateDoulaWorkshopBooking(CreateView):
    '''Page where people can sign up for Doula Training Workshops.'''

    model = DoulaWorkshopBooking
    form_class = DoulaWorkshopBookingForm
    template_name = 'doula_workshop_booking_form.html'
    # success_url = reverse_lazy('doula_training:success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        workshop_detail = DoulaWorkshop.objects.filter(pk=self.kwargs['pk'])
        context['workshop_detail'] = workshop_detail
        attendees = DoulaWorkshopBooking.objects.filter(workshop=self.kwargs['pk']).count()
        if attendees >= 10:
            context['message'] = 'Sorry, this workshop is full! Please choose another workshop to attend.'
        return context
        

    def get_initial(self, **kwargs):
        initial = super().get_initial(**kwargs)
        if self.request.method == 'GET':
            initial['location'] = self.kwargs['location']
            initial['workshop'] = self.kwargs['pk']
            return initial
        else:
            return initial

    def get_success_url(self):
        return reverse('doula_training:success', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        email = form.cleaned_data['email']
        workshop = form.cleaned_data['workshop']
        message = f"The following person has signed up for a class.\n\n \
        {name}\n \
        {email}\n \
        {phone}\n \
        Class: {workshop.title}\n \
        Starting: {workshop.start_date}\n\n \
        Login in for details: https://www.well-roundedmaternity.com/admin/doula_training/doulaworkshopbooking/"

        message2 = f"Thank you for signing up for a class with Well-Rounded Maternity! Details are below.\n\n \
        {name}\n \
        {email}\n \
        {phone}\n \
        Class: {workshop.title}\n \
        Starting: {workshop.start_date}\n \
        Ending: {workshop.end_date}\n \
        Location:\n \
        {workshop.location.location_name}\n \
        {workshop.location.location_address}\n \
        {workshop.location.location_city}, {workshop.location.location_state} {workshop.location.location_zip}\n\n"
        message2 += "If you have any questions, please contact Coral Slavin @ 262-893-9945. We look forward to seeing you in class!\n\n\nWell-Rounded Maternity"

        to_email = User.objects.get(id=2).email
        subject = 'Doula Workshop Booking'
        from_email = 'no-reply@well-roundedmaternity.com'
        try:
            send_mail(subject, message, from_email, [to_email])
            send_mail(subject, message2, from_email, [email])
        except BadHeaderError:
            pass

        return super().form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class DoulaWorkshopBookingSuccess(TemplateView):
    '''Redirect to template_name after successfully registering for doula training.'''

    template_name = 'doula_workshop_booking_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = DoulaWorkshopBooking.objects.get(id=kwargs['pk'])
        context['booking_detail'] = booking

        if booking.cost == 300:
            amount = 100
        else:
            amount = booking.cost

        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': amount,
            'item_name': booking.workshop.title,
            'invoice': f"dw{str(booking.pk)}",
            'currency_code': 'USD',
            'notify_url': self.request.build_absolute_uri(reverse('paypal-ipn')),
            'return': self.request.build_absolute_uri(reverse('payment-success')),
            'cancel_return': self.request.build_absolute_uri(reverse('doula_training:success', kwargs={'pk': booking.pk})),
            'custom': booking.pk,
        }

        # Paypal payment form instance.
        form = PayPalPaymentsForm(initial=paypal_dict)
        context['form'] = form

        context['request'] = self.request

        return context
