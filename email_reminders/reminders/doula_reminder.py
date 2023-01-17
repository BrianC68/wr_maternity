import sys
import os

if os.name == 'nt':
    sys.path.append("C:\\Users\\brian\\Documents\\wr_maternity\\")
else:
    sys.path.append("/home/wrmaternity/wr_maternity/")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wr_maternity.settings')

import django
django.setup()

from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from doula_training.models import DoulaWorkshopBooking, DoulaWorkshop
from email_reminders.models import ReminderEmail
from datetime import date, timedelta
from django.template.loader import render_to_string

# Add 14 days to current date to send 2 week reminder
the_date = date.today() + timedelta(days=14)

def send_doula_workshop_email_reminder(future_date):
    '''Sends doula training workshop email reminder 2 weeks prior to the first workshop.'''

    try:
        # Retrieve doula workshop info with start_date 2 weeks out
        dt_workshop = DoulaWorkshop.objects.filter(start_date=future_date)
        # Retrieve email addresses of people who are signed up for the class
        dt_workshop_attendees = DoulaWorkshopBooking.objects.filter(workshop=dt_workshop[0].id).values_list('email', flat=True)
        # Cast recipients object as a list
        recipients = list(dt_workshop_attendees)
    except:
        
        return

    # Build the plain text email message
    # {dt_workshop[0].location.location_name}
    # {dt_workshop[0].location.location_address}
    # {dt_workshop[0].location.location_city}, {dt_workshop[0].location.location_state} {dt_workshop[0].location.location_zip}

    message = f'''
    {dt_workshop[0].title}
    Remote via Zoom

    Class Starts: {dt_workshop[0].start_date.strftime('%b %d, %Y')}
    Last day of class: {dt_workshop[0].end_date.strftime('%b %d, %Y')}
    '''

    # Get ReminderEmail model fields
    email_info = ReminderEmail.objects.get(email_type='DOULA')
    subject = email_info.subject
    message += "\n" + strip_tags(email_info.message).replace('&nbsp;', '').replace('&#39;', "'")
    
    # Build the html email message from the template
    html_message = render_to_string(
        'dt_workshop_reminder_email.html',
        {
            'dt_workshop': dt_workshop,
            'message': email_info.message,
        }
    )
    # print(html_message)

    # Try to send the email to the list of recipients
    try:
        for recipient in recipients:
            mail = EmailMultiAlternatives(
                subject, message, 'coral.slavin@gmail.com', [recipient]
            )
            mail.attach_alternative(html_message, "text/html")
            mail.send()
    except:
        return

    # If all goes well, return
    return