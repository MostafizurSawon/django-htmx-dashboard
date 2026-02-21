from django.shortcuts import render

def dashboard(request):
    # আপনার ড্যাশবোর্ডের ডেটা
    context = {'title': 'Dashboard Overview'}
    
    # যদি রিকোয়েস্ট HTMX থেকে আসে, শুধু ভেতরের অংশটুকু পাঠাবো
    if request.htmx:
        return render(request, 'pages/dashboard.html', context)
    
    # ব্রাউজারে রিফ্রেশ দিলে base.html সহ পুরো পেজ পাঠাবো
    return render(request, 'pages/dashboard_full.html', context)