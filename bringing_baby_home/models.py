from django.db import models
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

from datetime import time


class BringingBabyHomeClass(models.Model):
    '''Model that holds class details.'''

    # Choices for class type
    BRINGING_BABY_HOME = '8_Week'
    SURVIVING_TO_THRIVING = '4_Week'

    CLASS_TYPE_CHOICES = [
        (BRINGING_BABY_HOME, 'Bringing Baby Home'),
        (SURVIVING_TO_THRIVING, 'Surviving to Thriving')
    ]

    # Model fields
    title = models.CharField(max_length=200, default="Gottman Bringing Baby Home Program")
    class_type = models.CharField(
        max_length=25,
        choices=CLASS_TYPE_CHOICES
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(default=time(19, 30))
    end_time = models.TimeField(default=time(21, 00))
    price = models.IntegerField(default=250)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ['-start_date']
        unique_together = [['start_date', 'end_date']]
        verbose_name = 'Bringing Baby Home Classe'


    def __str__(self):
        return f"{self.title}, {self.start_date}, {self.get_class_type_display()}"


class BringingBabyHomeClassBooking(models.Model):
    '''Model that holds Bringing Baby Home class participants'''

    # Model fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    partner_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    phone = PhoneNumberField()
    bbh_class = models.ForeignKey(BringingBabyHomeClass, on_delete=models.CASCADE, related_name='bbh_booking', null=True)
    cost = models.IntegerField(null=True, blank=True)
    paid = models.IntegerField(null=True, blank=True)

    class Meta:
        # Default ordering is by last name ascending
        ordering = ['last_name']
        unique_together = ['first_name', 'last_name', 'email', 'bbh_class']
        verbose_name = 'Bringing Baby Home Class Booking'
    