from django.urls import path
from . import views

urlpatterns = [
    # ড্যাশবোর্ডের মূল রাউট
    path('dashboard/', views.dashboard_view, name='dashboard'),
]