from django.apps import AppConfig

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    # এখানে আপনার ফোল্ডারের নামসহ অ্যাপের পাথ দিতে হবে। 
    # যদি ফোল্ডারের নাম 'app' হয়, তাহলে:
    name = 'apps.accounts' 
    
    # কিন্তু জ্যাঙ্গোর কাছে অ্যাপের লেবেল (app_label) হবে শুধু 'accounts'। 
    # এটি না দিলে ডাটাবেস টেবিলের নামে ঝামেলা হতে পারে।
    label = 'accounts'