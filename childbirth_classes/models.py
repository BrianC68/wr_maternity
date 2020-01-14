from django.db import models
from django.utils.text import slugify
from locations.models import Location
from phone_field import PhoneField

from datetime import time


class ChildbirthClass(models.Model):
    '''Model that holds childbirth class details.'''

    # Choices for class type
    COMPREHENSIVE = 'COMP'
    CONDENSED = 'COND'

    CLASS_TYPE_CHOICES = [
        (COMPREHENSIVE, 'Comprehensive'),
        (CONDENSED, 'Condensed')
    ]

    # Model fields
    title = models.CharField(max_length=200, default="Well-Rounded Childbirth Class")
    class_type = models.CharField(
        max_length=25,
        choices=CLASS_TYPE_CHOICES
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField(default=time(16, 30))
    end_time = models.TimeField(default=time(21, 0))
    location = models.ForeignKey(Location, default=3, on_delete=models.CASCADE, related_name='cb_location', null=True)
    price = models.IntegerField(default=275)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        ordering = ['-start_date']
        unique_together = [['start_date', 'end_date']]
        verbose_name = 'Childbirth Classe'


    def __str__(self):
        return f"{self.title}, {self.start_date}"


class ChildbirthClassBooking(models.Model):
    '''Model that holds childbirth class participants'''

    # Model fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    phone = PhoneField()
    cb_class = models.ForeignKey(ChildbirthClass, on_delete=models.CASCADE, related_name='cb_booking', null=True)
    cost = models.IntegerField(null=True, blank=True)
    paid = models.IntegerField(null=True, blank=True)

    class Meta:
        # Default ordering is by last name ascending
        ordering = ['last_name']
        unique_together = ['first_name', 'last_name', 'email', 'cb_class']