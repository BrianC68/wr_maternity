from django.contrib import admin
from .models import ChildbirthClass, ChildbirthClassBooking


class ChildbirthClassAdmin(admin.ModelAdmin):
    '''Change the display of the model in the admin interface.'''
    # put fields in the order in which you want them ordered in admin
    # fields = ['title', 'start_date', 'end_date', 'is_active']
    # adds search functionality to database table
    # search_fields = []
    # adds filters to right side of admin dbase pages
    # list_filter = []
    # adds more fields to admin view
    list_display = ['title', 'class_type', 'start_date', 'end_date', 'location', 'is_active']
    # list_display_links = []
    # list_editable = ['is_active']
    prepopulated_fields = {'slug': ('title', 'start_date')}


class ChildbirthClassBookingAdmin(admin.ModelAdmin):
    '''Change the display of the model in the admin interface.'''
    # adds more fields to admin view
    list_display = ['last_name', 'first_name', 'cb_class', 'cost', 'paid']

# Register the models so they show up in admin
admin.site.register(ChildbirthClass, ChildbirthClassAdmin)
admin.site.register(ChildbirthClassBooking, ChildbirthClassBookingAdmin)
