from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Hotel

@admin.register(Hotel)
class HotelAdmin(ModelAdmin):
    list_display = ("name", "owner", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "owner__email", "owner__phone_number")
    ordering = ("-created_at",)