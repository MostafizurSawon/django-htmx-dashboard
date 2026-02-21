from django.db import models
from apps.hotels.models import Hotel
from django.utils import timezone

class Plan(models.Model):
    BILLING_TYPES = (
        ('MONTHLY', 'Monthly'),
        ('YEARLY', 'Yearly'),
        ('PER_BOOKING', 'Per Booking'),
    )
    
    name = models.CharField(max_length=100) # e.g., Basic, Premium, Pay-as-you-go
    billing_type = models.CharField(max_length=20, choices=BILLING_TYPES)
    base_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Default price for this plan")
    
    def __str__(self):
        return f"{self.name} ({self.get_billing_type_display()})"


class Subscription(models.Model):
    STATUS_CHOICES = (
        ('ACTIVE', 'Active'),
        ('WARNING', 'Warning (Payment Due)'),
        ('EXPIRED', 'Expired'),
    )

    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, related_name='subscription')
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    
    # Custom Price: যদি কোনো নির্দিষ্ট হোটেলের জন্য দাম কাস্টমাইজ করতে হয়
    custom_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        help_text="Override base price for this specific hotel."
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ACTIVE')
    # start_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True) # Per booking এর ক্ষেত্রে এটি null থাকতে পারে

    def __str__(self):
        return f"{self.hotel.name} - {self.plan.name if self.plan else 'No Plan'}"

    # প্রপার্টি মেথড: এটি চেক করবে কাস্টম প্রাইস আছে কি না, না থাকলে বেস প্রাইস রিটার্ন করবে
    @property
    def current_price(self):
        if self.custom_price is not None:
            return self.custom_price
        return self.plan.base_price if self.plan else 0