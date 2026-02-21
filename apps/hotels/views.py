from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# ১. মেইন ড্যাশবোর্ড ভিউ (SPA Entry Point)


@login_required
def dashboard_view(request):
    context = {'title': 'Dashboard Overview'}
    
    # শুধুমাত্র যদি HTMX রিকোয়েস্ট হয় এবং সেটি নির্দিষ্টভাবে 'main-content' কে টার্গেট করে
    if request.htmx and request.htmx.target == "main-content":
        return render(request, 'pages/dashboard.html', context)
    
    # লগইন করার পর বা সরাসরি ইউআরএল এন্টার দিলে এই পুরো পেজটি লোড হবে
    return render(request, 'pages/dashboard_full.html', context)


# ২. সাবস্ক্রিপশন ওয়ার্নিং পেজ
@login_required
def billing_warning_view(request):
    """
    যাদের সাবস্ক্রিপশন শেষ, মিডলওয়্যার তাদের এই পেজে পাঠিয়ে দেবে।
    """
    return render(request, 'billing/warning.html')