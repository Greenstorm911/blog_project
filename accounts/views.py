from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout


def accounts(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request , username=username,password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('/admin')
            return redirect('/')
        else:
            return render(request, 'accounts/accounts.html')
        
        
    return render(request, 'accounts/accounts.html')

def regester(request):
    if not request.user.is_anonymous:
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        newuser = User.objects.create_user(username, email, password)
        newuser.save()
        login(request,newuser)
        return redirect('/')
    return render(request, 'accounts/regester.html')


