from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from datetime import time

class MakingMarriageWorkClass(models.Model):
    '''Model that holds class details.'''

    # Model fields
    title = models.CharField(max_length=200, default="Gottman Seven Principles Program")
    class_date = models.DateField(unique=True)
    start_time = models.TimeField(default=time(9, 00))
    end_time = models.TimeField(default=time(17, 30))
    price = models.IntegerField(default=300)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        # Default ordering is in descending start date order
        ordering = ['-class_date']

    def __str__(self):
        return f"{self.title}, {self.class_date}"


class MakingMarriageWorkClassBooking(models.Model):
    '''Model that holds class bookings'''

    # Model fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    phone = PhoneNumberField()
    mmw_class = models.ForeignKey(MakingMarriageWorkClass, on_delete=models.CASCADE, related_name='mmw_booking', blank=True, null=True)
    cost = models.IntegerField(null=True, blank=True)
    paid = models.IntegerField(null=True, blank=True)

    class Meta:
        # Default ordering is by last name ascending
        ordering = ['last_name']
        unique_together = ['first_name', 'last_name', 'email', 'mmw_class']
