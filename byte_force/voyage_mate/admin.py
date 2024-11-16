from django.contrib import admin


# Register your models here.
from .models import Destination

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination', 'rating', 'created_at') 
    search_fields = ('user__username', 'destination__name')  # Enable search by user's username and destination name
    list_filter = ('rating', 'destination')  # Enable filtering by rating and destination
    ordering = ('-created_at',)  # Default ordering by created_at in descending order
    raw_id_fields = ('destination',)  # Use raw ID field for the destination 