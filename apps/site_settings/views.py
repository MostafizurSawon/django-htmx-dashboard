from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Contact

def contact_list(request):
    query = request.GET.get('q', '')
    contacts = Contact.objects.all()

    # Search Logic
    if query:
        contacts = contacts.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query) |
            Q(subject__icontains=query)
        )

    # Pagination Logic (প্রতি পেজে ১০ জন)
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }

    # HTMX রিকোয়েস্ট (SPA)
    if request.htmx:
        return render(request, 'site_settings/contact_list.html', context)
    
    # ব্রাউজারে ডিরেক্ট হিট করলে
    return render(request, 'site_settings/contact_list_full.html', context)