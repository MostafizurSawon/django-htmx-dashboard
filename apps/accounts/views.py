from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):
    # ইউজার যদি আগে থেকেই লগইন করা থাকে, তবে তাকে ড্যাশবোর্ডে পাঠিয়ে দাও
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        # এখানে 'username' ফিল্ডটি ইমেইল অথবা ফোন নম্বর যেকোনো একটি হতে পারে
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')

        # আমাদের কাস্টম ব্যাকএন্ড এটি হ্যান্ডেল করবে
        user = authenticate(request, username=identifier, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "ইমেইল/ফোন নম্বর অথবা পাসওয়ার্ড ভুল।")

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')