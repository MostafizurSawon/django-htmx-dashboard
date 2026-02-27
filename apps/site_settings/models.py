from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.name
    
    



# ==================== Bangladesh Location Models ====================
class BD_Division(models.Model):
    name = models.CharField(max_length=100, unique=True)
    name_bn = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "BD Divisions"


class BD_District(models.Model):
    division = models.ForeignKey(BD_Division, on_delete=models.CASCADE, related_name='districts')
    name = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name} ({self.division.name})"

    class Meta:
        unique_together = ('division', 'name')
        ordering = ['name']
        verbose_name_plural = "BD Districts"


class BD_Upazila(models.Model):
    district = models.ForeignKey(BD_District, on_delete=models.CASCADE, related_name='upazilas')
    name = models.CharField(max_length=100)
    name_bn = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        # unique_together = ('district', 'name')
        ordering = ['name']
        verbose_name_plural = "BD Upazilas"

 
# ==================== Main Model for Marketing (Hospitality) ====================
class Hospitality(models.Model):
    hospitality_id = models.CharField(max_length=20, unique=True, verbose_name="ID (e.g., BD-DHA-00001)")
    name = models.CharField(max_length=255, verbose_name="Name")

    # Location (ForeignKey)
    division = models.ForeignKey(BD_Division, on_delete=models.SET_NULL, null=True, blank=True, related_name='hospitalities')
    district = models.ForeignKey(BD_District, on_delete=models.SET_NULL, null=True, blank=True, related_name='hospitalities')
    upazila = models.ForeignKey(BD_Upazila, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Upozila/Thana", related_name='hospitalities')

    postcode = models.CharField(max_length=10, blank=True)
    address = models.TextField()
    landmark = models.CharField(max_length=255, blank=True)

    # Contact & Management
    manager_owner_name = models.CharField(max_length=255, blank=True, verbose_name="Manager/Owner Name")
    manager_phone = models.CharField(max_length=20, blank=True)
    primary_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    facebook = models.URLField(blank=True)
    google_maps_link = models.URLField(blank=True, verbose_name="Google Maps Link")
    website = models.URLField(blank=True)
    other_link = models.URLField(blank=True, verbose_name="Other Link")

    # Pricing
    rent_range = models.CharField(max_length=100, blank=True, verbose_name="Rent Range (TK)")
    rent_category = models.CharField(
        max_length=50, 
        blank=True, 
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')]
    )

    # Rating
    star_rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1, 
        null=True, 
        blank=True,
        verbose_name="Star Rating (e.g. 4.5)"
    )
    average_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, editable=False)
    rating_count = models.PositiveIntegerField(default=0, editable=False)

    # Extra for marketing form
    hotel_type = models.CharField(max_length=100, blank=True, verbose_name="Type (Hotel/Resort/Guest House etc.)")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.hospitality_id})"

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Hospitalities"