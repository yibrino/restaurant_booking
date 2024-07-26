# main/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'homepage.html')

def customer_page(request):
    return render(request, 'customer.html')

def about_page(request):
    return render(request, 'about.html')

def admin_page(request):
    return render(request, 'admin.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
def customer_dashboard(request):
    return render(request, 'customer_dashboard.html') 

def customer_register(request):
    return render(request, 'register_customer.html') 

