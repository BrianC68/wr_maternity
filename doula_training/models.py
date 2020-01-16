from django.db import models
from locations.models import Location
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

class DoulaWorkshop(models.Model):
    '''Model that holds doula workshop details.'''

    # Model fields
    title = models.CharField(max_length=200, default="Doula Training Workshop")
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location', default=1)
    full_price = models.IntegerField(default=300)
    discount_price = models.IntegerField(default=275)
    deposit = models.IntegerField(default=100)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        # Default ordering is in descending start date order
        ordering = ['-start_date']
        # These fields must be unique together for each workshop
        unique_together = [['start_date', 'end_date']]

    def __str__(self):
        return f"{self.title}, {self.start_date}"


class DoulaWorkshopBooking(models.Model):
    '''Model that holds doula workshop participants'''

    # Model fields
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=5)
    phone = PhoneNumberField()
    workshop = models.ForeignKey(DoulaWorkshop, on_delete=models.CASCADE, related_name='doula_booking', blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='booking_location', default=1)
    cost = models.IntegerField(null=True, blank=True)
    paid = models.IntegerField(null=True, blank=True)

    class Meta:
        # Default ordering is by last name ascending
        ordering = ['last_name']
        unique_together = ['first_name', 'last_name', 'email', 'workshop']
