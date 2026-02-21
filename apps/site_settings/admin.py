from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline  
from .models import Contact

# site_settings/apps.py
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class SiteSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_settings'  # তোমার app_label

    verbose_name = _(" ")          # ← খালি স্পেস বা শুধু "" দাও → header অদৃশ্য/খালি হবে
    # অথবা verbose_name = ""       # পুরোপুরি খালি
    # অথবা verbose_name = _("Site Settings")  # যদি চাও এই নাম দেখাক (তোমার পছন্দ)

@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    list_display = ["name", "phone", "email", "subject", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "email", "subject", "description"]
    ordering = ["-created_at"]

    # Optional: ফিল্ডগুলোকে সুন্দর করে গ্রুপ করতে পারো
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
            "classes": ("collapse",),  # unfold-এ collapse সুন্দর দেখায়
        }),
    )

    readonly_fields = ("created_at", "updated_at")