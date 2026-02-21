from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# ১. Custom User Manager
class UserManager(BaseUserManager):
    def create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        # ইমেইল অথবা ফোন নম্বর যেকোনো একটি অবশ্যই থাকতে হবে
        if not email and not phone_number:
            raise ValueError('ইউজারের একটি ইমেইল অ্যাড্রেস অথবা ফোন নম্বর থাকতে হবে।')
        
        if email:
            email = self.normalize_email(email)
            
        user = self.model(email=email, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, phone_number=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser-এর অবশ্যই is_staff=True থাকতে হবে।')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser-এর অবশ্যই is_superuser=True থাকতে হবে।')

        # সুপারইউজার তৈরির সময় ডিফল্ট ইমেইল বা ফোন নম্বর ডিল করার লজিক
        return self.create_user(email, phone_number, password, **extra_fields)


# ২. Custom User Model
class User(AbstractUser):
    # জ্যাঙ্গোর ডিফল্ট username ফিল্ড আমরা বাদ দিয়ে দিচ্ছি
    username = None 
    
    email = models.EmailField('Email Address', unique=True, null=True, blank=True)
    phone_number = models.CharField('Phone Number', max_length=15, unique=True, null=True, blank=True)
    
    # SaaS-এর জন্য প্রাথমিক কিছু ফিল্ড রাখতে পারি (Role Management-এর সুবিধার্থে)
    is_hotel_admin = models.BooleanField(default=False)
    is_receptionist = models.BooleanField(default=False)

    # লগইন করার প্রাইমারি ফিল্ড হিসেবে ইমেইল সেট করছি, তবে Auth Backend দিয়ে ফোন নম্বরও কাজ করবে
    USERNAME_FIELD = 'email' 
    # REQUIRED_FIELDS ফাঁকা রাখছি কারণ Manager-এ আমরা কাস্টম ভ্যালিডেশন দিয়েছি
    REQUIRED_FIELDS = [] 

    objects = UserManager()

    def __str__(self):
        return self.email if self.email else str(self.phone_number)