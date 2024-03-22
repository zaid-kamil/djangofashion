from django.shortcuts import render

# Create your views here.
def customer_login(request):
    return render(request, 'accounts/customer/login.html')
def seller_login(request):
    return render(request, 'accounts/seller/login.html')
def customer_register(request):
    return render(request, 'accounts/customer/register.html')
def seller_register(request):
    return render(request, 'accounts/seller/register.html')