from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Plan, Subscription

@admin.register(Plan)
class PlanAdmin(ModelAdmin):
    list_display = ("name", "billing_type", "base_price")
    list_filter = ("billing_type",)
    search_fields = ("name",)

@admin.register(Subscription)
class SubscriptionAdmin(ModelAdmin):
    list_display = ("hotel", "get_plan_name", "status", "start_date", "end_date")
    list_filter = ("status", "plan__billing_type")
    search_fields = ("hotel__name",)
    
    # Custom Price এবং Base Price সুন্দরভাবে দেখানোর জন্য
    fieldsets = (
        ("Hotel & Plan", {
            "fields": ("hotel", "plan", "status")
        }),
        ("Pricing Configuration", {
            "fields": ("custom_price",),
            "description": "Leave custom price blank to use the plan's default base price."
        }),
        ("Dates", {
            "fields": ("start_date", "end_date")
        }),
    )
    # readonly_fields = ("start_date",)

    def get_plan_name(self, obj):
        return obj.plan.name if obj.plan else "No Plan"
    get_plan_name.short_description = "Plan"