# apps/hotels/mixins.py
from django.db import models
from django.core.exceptions import PermissionDenied

class TenantMixin(models.Model):
    """
    SaaS এর সব মডেল (Room, Booking) এই Mixin ব্যবহার করবে।
    """
    hotel = models.ForeignKey('hotels.Hotel', on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def has_permission(self, user):
        # চেক করবে ইউজার কি এই হোটেলের মালিক বা স্টাফ?
        return user.owned_hotels.filter(id=self.hotel_id).exists()