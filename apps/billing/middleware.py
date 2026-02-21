from django.shortcuts import redirect
from django.utils import timezone

class SubscriptionCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # যেসব URL-এ এই মিডলওয়্যার আটকাবে না (যেমন: admin panel, logout বা warning page)
        # যাতে বিলিং পেজেও লুপে পড়ে না যায়
        exempt_urls = ['/admin/', '/logout/', '/billing-warning/']
        
        # ইউজার যদি লগইন করা থাকে এবং সে যদি সুপারইউজার (আপনার মতো) না হয়
        if request.user.is_authenticated and not request.user.is_superuser:
            
            # বর্তমান রিকোয়েস্টের URL যদি exempt_urls এর লিস্টে না থাকে
            if not any(request.path.startswith(url) for url in exempt_urls):
                
                # ইউজারের হোটেল খোঁজা (related_name 'owned_hotels' ব্যবহার করে)
                hotel_qs = request.user.owned_hotels.all()
                
                if hotel_qs.exists():
                    hotel = hotel_qs.first()
                    
                    # হোটেলের সাবস্ক্রিপশন চেক করা
                    if hasattr(hotel, 'subscription'):
                        subscription = hotel.subscription
                        
                        # যদি সাবস্ক্রিপশন EXPIRED থাকে অথবা আজকের দিনের চেয়ে end_date পার হয়ে যায়
                        if subscription.status == 'EXPIRED' or (
                            subscription.end_date and subscription.end_date < timezone.now().date()
                        ):
                            # তাকে জোর করে বিলিং ওয়ার্নিং পেজে পাঠিয়ে দেওয়া হবে
                            return redirect('/billing-warning/')
                else:
                    # যদি ইউজারের কোনো হোটেলই অ্যাসাইন করা না থাকে, তবে তাকেও ওয়ার্নিং দেওয়া যায়
                    pass 

        response = self.get_response(request)
        return response