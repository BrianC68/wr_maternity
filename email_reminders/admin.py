from django.contrib import admin
from .models import ReminderEmail

class ReminderEmailAdmin(admin.ModelAdmin):
    # Add fields to admin model view
    list_display = ['email_type', 'subject']

admin.site.register(ReminderEmail, ReminderEmailAdmin)
