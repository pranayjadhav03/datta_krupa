# main/admin.py

from django.contrib import admin
from .models import Booking, RefurbishedLaptop

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'issue_type', 'message', 'created_at')
    list_filter = ('created_at',)


@admin.register(RefurbishedLaptop)
class RefurbishedLaptopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'price', 'available')
    list_filter = ('available',)
