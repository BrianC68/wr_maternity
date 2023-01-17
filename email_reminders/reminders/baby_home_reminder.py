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
# from django.contrib.auth.models import User
from django.utils.html import strip_tags
from bringing_baby_home.models import BringingBabyHomeClass, BringingBabyHomeClassBooking
from email_reminders.models import ReminderEmail
from datetime import date, timedelta
from django.template.loader import render_to_string

# Add 14 days to current date to send 2 week reminder
the_date = date.today() + timedelta(days=14)


def send_bringing_baby_home_class_email_reminder(future_date):
    '''Sends bringing baby home class email reminder 2 weeks prior to the first class.'''

    try:
        # Retrieve bringing baby home class info with start_date 2 weeks out
        bbh_class = BringingBabyHomeClass.objects.filter(start_date=future_date)
        # Retrieve email addresses of people who are signed up for the class
        bbh_class_attendees = BringingBabyHomeClassBooking.objects.filter(bbh_class=bbh_class[0].id).values_list('email', flat=True)
        # Cast recipients object as a list
        recipients = list(bbh_class_attendees)
    except:
        return

    message = f'''
    {bbh_class[0].title}
    Remote via Zoom

    Class Starts: {bbh_class[0].start_date.strftime('%b %d, %Y')} at {bbh_class[0].start_time.strftime('%I:%M %p')} till {bbh_class[0].end_time.strftime('%I:%M %p')}
    Class Ends: {bbh_class[0].end_date.strftime('%b %d, %Y')}
    '''

    # Get ReminderEmail model fields
    email_info = ReminderEmail.objects.get(email_type='BBHCLASS')
    subject = email_info.subject
    message += "\n" + strip_tags(email_info.message).replace('&nbsp;', '').replace('&#39;', "'")

    # Build the html email message from the template
    html_message = render_to_string(
        '../templates/bbh_class_reminder_email.html',
        {
            'bbh_class': bbh_class,
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