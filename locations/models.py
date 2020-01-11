from django.db import models


class Location(models.Model):
    '''Holds locations where classes are taught.'''

    # Model Fields
    location_name = models.CharField(max_length=200)
    location_address = models.CharField(max_length=200)
    location_city = models.CharField(max_length=50)
    location_state = models.CharField(max_length=2)
    location_zip = models.CharField(max_length=5)
    location_lng = models.DecimalField(decimal_places=15, max_digits=18, null=True)
    location_lat = models.DecimalField(decimal_places=15, max_digits=18, null=True)

    class Meta:
        unique_together = [['location_name', 'location_address']]
        ordering = ['location_name']

    def __str__(self):
        return f"{self.location_name}"
