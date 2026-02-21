"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .import views
from apps.billing.views import billing_warning_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # সাবস্ক্রিপশন শেষ হলে ওয়ার্নিং পেজ
    path('billing-warning/', billing_warning_view, name='billing_warning'),
    
    # আপনার Hotels অ্যাপের সব URL (যেখানে ড্যাশবোর্ড আছে)
    path('', include('apps.hotels.urls')),

    path('dashboard/', include('apps.site_settings.urls'))
]
