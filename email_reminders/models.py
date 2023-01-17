from django.db import models
from ckeditor.fields import RichTextField


class ReminderEmail(models.Model):
    '''This model holds the Subject and Message for the reminder email sent two weeks before class or workshop.'''

    app_label = 'email_reminders'
    
    # Choices for email_type, database values
    DOULA_WORKSHOP = 'DOULA'
    CHILDBIRTH_CLASS = 'CBCLASS'
    BRINGING_BABY_HOME = 'BBHCLASS'
    MAKING_MARRIAGE_WORK = 'MMWCLASS'

    # String representations of choices
    EMAIL_TYPE_CHOICES = [
        (DOULA_WORKSHOP, 'Doula Workshop'),
        (CHILDBIRTH_CLASS, 'Childbirth Class'),
        (BRINGING_BABY_HOME, 'Bringing Baby Home'),
        (MAKING_MARRIAGE_WORK, 'Making Marriage Work'),
    ]

    #Model Fields
    email_type = models.CharField(max_length=25, unique=True, choices=EMAIL_TYPE_CHOICES)
    subject = models.CharField(max_length=100)
    message = RichTextField()
