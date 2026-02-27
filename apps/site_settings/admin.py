from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import BD_District, BD_Division, BD_Upazila, Contact, Hospitality


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ["name", "phone", "email", "subject", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "email", "subject", "description"]
    ordering = ["-created_at"]

    fieldsets = (
        ("Basic Information", {
            "fields": ("name", "phone", "email", "subject"),
            "classes": ("wide",),
        }),
        ("Message", {
            "fields": ("description",),
            "classes": ("wide",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at", "updated_at")


@admin.register(Hospitality)
class HospitalityAdmin(ModelAdmin):
    list_display = [
        "hospitality_id",
        "name",
        "division",
        "district",
        "upazila",
        "primary_phone",
        "star_rating",
        "rent_category",
        "created_at",
    ]
    list_filter = [
        "division",
        "district",
        "rent_category",
        "star_rating",
        "hotel_type",
        "created_at",
    ]
    search_fields = [
        "hospitality_id",
        "name",
        "address",
        "primary_phone",
        "manager_owner_name",
        "email",
    ]
    ordering = ["name"]
    list_per_page = 25

    fieldsets = (
        ("Basic Information", {
            "fields": (
                "hospitality_id",
                "name",
                "hotel_type",
                "star_rating",
            ),
            "classes": ("wide",),
        }),
        ("Location", {
            "fields": (
                "division",
                "district",
                "upazila",
                "postcode",
                "address",
                "landmark",
                "google_maps_link",
            ),
            "classes": ("wide",),
        }),
        ("Contact & Management", {
            "fields": (
                "manager_owner_name",
                "manager_phone",
                "primary_phone",
                "secondary_phone",
                "whatsapp",
                "email",
                "facebook",
            ),
            "classes": ("wide",),
        }),
        ("Online Presence & Pricing", {
            "fields": (
                "website",
                "other_link",
                "rent_range",
                "rent_category",
            ),
            "classes": ("wide",),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at", "average_rating", "rating_count"),
            "classes": ("collapse",),
        }),
    )

    readonly_fields = ("created_at", "updated_at", "average_rating", "rating_count")

    # Optional: যদি অনেক ডেটা হয় তাহলে
    # autocomplete_fields = ['division', 'district', 'upazila']


@admin.register(BD_Division)
class DivisionAdmin(ModelAdmin):
    list_display = ["name", "name_bn"]
    search_fields = ["name", "name_bn"]
    ordering = ["name"]


@admin.register(BD_District)
class DistrictAdmin(ModelAdmin):
    list_display = ["name", "division", "name_bn"]
    list_filter = ["division"]
    search_fields = ["name", "name_bn"]
    ordering = ["name"]


@admin.register(BD_Upazila)
class UpazilaAdmin(ModelAdmin):
    list_display = ["name", "district", "name_bn"]
    list_filter = ["district"]
    search_fields = ["name", "name_bn"]
    ordering = ["name"]