from django.db import models
from django.utils.text import slugify
from phone_field import PhoneField
from ckeditor.fields import RichTextField


class Midwife(models.Model):
    '''This model holds information on midwives.'''

    # Choices for website_type
    WEBSITE = 'WEB'
    PROFILE = 'PROF'
    FACEBOOK = 'FB'

    WEBSITE_TYPE_CHOICES = [
        (WEBSITE, 'Website'),
        (PROFILE, 'Profile'),
        (FACEBOOK, 'Facebook')
    ]

    # Model Fields
    name = models.CharField(max_length=100)
    description = RichTextField(null=True, blank=True)
    photo = models.ImageField(upload_to='midwives')
    service_area = models.CharField(max_length=100)
    email = models.EmailField()
    phone = PhoneField(null=True)
    website_type = models.CharField(null=True, blank=True, max_length=25, choices=WEBSITE_TYPE_CHOICES)
    website_text = models.CharField(null=True, blank=True, max_length=100)
    website_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True)

    class Meta:
        # Default ordering
        ordering = ['name']
        # Unique fields
        unique_together = [['name', 'email', 'phone']]

    def __str__(self):
        return f"{self.name}, {self.phone}, {self.email}"

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
