from django.contrib import admin
from .models import BringingBabyHomeClass, BringingBabyHomeClassBooking


class BringingBabyHomeClassAdmin(admin.ModelAdmin):
    '''Change the display of the model in the admin interface.'''
    # adds more fields to admin view
    list_display = ['title', 'class_type', 'start_date', 'end_date', 'is_active']
    prepopulated_fields = {'slug': ('title', 'start_date')}


class BringingBabyHomeClassBookingAdmin(admin.ModelAdmin):
    '''Change the display of the model in the admin interface.'''
    # adds more fields to admin view
    list_display = ['last_name', 'first_name', 'bbh_class', 'cost', 'paid']

# Register the models so they show up in admin
admin.site.register(BringingBabyHomeClass, BringingBabyHomeClassAdmin)
admin.site.register(BringingBabyHomeClassBooking, BringingBabyHomeClassBookingAdmin)
