from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    # এডিট পেজের (Change view) কনফিগারেশন (আগেরটাই থাকবে)
    fieldsets = (
        ("Login Credentials", {"fields": ("email", "phone_number", "password")}),
        ("Role & Permissions", {"fields": ("is_hotel_admin", "is_receptionist", "is_staff", "is_superuser", "is_active")}),
    )
    
    # --- নতুন যুক্ত করা অংশ (Add view এরর ফিক্স) ---
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "phone_number", "password1", "password2"),
        }),
    )
    # ----------------------------------------------

    list_display = ("email", "phone_number", "is_hotel_admin", "is_active")
    search_fields = ("email", "phone_number")
    ordering = ("email",)
    
    filter_horizontal = ()
    list_filter = ()