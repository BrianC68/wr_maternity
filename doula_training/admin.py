from django.contrib import admin
from .models import DoulaWorkshop, DoulaWorkshopBooking
# Register your models here.


class DoulaWorkshopAdmin(admin.ModelAdmin):
    # put fields in the order in which you want them ordered in admin
    # fields = ['title', 'start_date', 'end_date', 'is_active']
    # adds search functionality to database table
    # search_fields = []
    # adds filters to right side of admin dbase pages
    # list_filter = []
    # adds more fields to admin view
    list_display = ['title',  'start_date', 'end_date', 'is_active']
    # list_display_links = []
    # list_editable = ['is_active']
    prepopulated_fields = {'slug': ('title', 'start_date')}


class DoulaWorkshopBookingAdmin(admin.ModelAdmin):
    # adds more fields to admin view
    list_display = ['last_name', 'first_name', 'workshop', 'cost', 'paid']


admin.site.register(DoulaWorkshop, DoulaWorkshopAdmin)
admin.site.register(DoulaWorkshopBooking, DoulaWorkshopBookingAdmin)
