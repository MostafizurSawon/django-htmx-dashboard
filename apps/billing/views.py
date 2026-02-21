from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def billing_warning_view(request):
    """
    সাবস্ক্রিপশন শেষ হয়ে গেলে ইউজারকে এই পেজটি দেখানো হবে।
    """
    return render(request, 'billing/warning.html')