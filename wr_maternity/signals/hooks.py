from django.shortcuts import get_object_or_404
from wr_maternity import settings
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from doula_training.models import DoulaWorkshopBooking
from childbirth_classes.models import ChildbirthClassBooking

def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    # print(kwargs)
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            return

        # Determine which model the payment is for
        if ipn_obj.invoice[:2] == 'dw':
            model = DoulaWorkshopBooking
        else:
            model = ChildbirthClassBooking

        # Update the booking with the paid amount.
        update_booking = model.objects.filter(id=ipn_obj.custom).update(paid=ipn_obj.mc_gross)
        
    else:
        print("Payment status was not ST_PP_COMPLETED.")

valid_ipn_received.connect(show_me_the_money)
