from django.contrib import admin
from .models import MakingMarriageWorkClass, MakingMarriageWorkClassBooking


class MakingMarriageWorkClassAdmin(admin.ModelAdmin):
    list_display = ['title', 'class_date', 'price', 'is_active']
    prepopulated_fields = {'slug': ('title', 'class_date')}


class MakingMarriageWorkClassBookingAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'mmw_class', 'cost', 'paid']


admin.site.register(MakingMarriageWorkClass, MakingMarriageWorkClassAdmin)
admin.site.register(MakingMarriageWorkClassBooking, MakingMarriageWorkClassBookingAdmin)
