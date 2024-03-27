from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def customer_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group') # customer
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Invalid credentials')
                redirect('clogin')
            else:
                # if user is a customer
                if user.groups.filter(name=group).exists():
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, 'You are not a customer')
                    return redirect('clogin')
        else:
            messages.error(request, 'Please fill all fields')
    return render(request, 'accounts/customer/login.html')
def seller_login(request):
    return render(request, 'accounts/seller/login.html')
def customer_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('clogin')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/customer/register.html')
def seller_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']
        group = request.POST['group']
        if pwd1 == pwd2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=pwd1)
                user.save()
                group = Group.objects.get(name=group)
                user.groups.add(group)
                messages.success(request, 'Account successfully created')
                return redirect('slogin')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/seller/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')