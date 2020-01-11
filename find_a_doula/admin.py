from django.contrib import admin
from .models import Doula


class DoulaAdmin(admin.ModelAdmin):
    # put fields in the order in which you want them ordered in admin
    # fields = ['title', 'start_date', 'end_date', 'is_active']
    # adds search functionality to database table
    # search_fields = []
    # adds filters to right side of admin dbase pages
    # list_filter = []
    # adds more fields to admin view
    list_display = ['name', 'email', 'phone']
    # list_display_links = []
    # list_editable = ['is_active']
    # Prepopulates the slug field
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Doula, DoulaAdmin)
