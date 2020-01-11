from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Page(models.Model):
    '''Page Model holds web page content.'''

    #Model fields
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    content = RichTextUploadingField()

    def __str__(self):
        return f"{self.title}"
