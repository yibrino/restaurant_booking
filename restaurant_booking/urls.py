"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from main.views import homepage,customer_page,admin_page,admin_dashboard,customer_dashboard,customer_register,about_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('api/',include('customers.urls')),
    path('api/',include('tablelist.urls')),
    path('api/',include('booktable.urls')),
     path('', homepage, name='homepage'), 
    path('about/', about_page, name='about_page'),
 
      path('customer/', customer_page, name='customer_page'),
    path('adminlogin/', admin_page, name='admin_page'),# Set the homepage view as the root URL
        path('adminlogin/dashboard/', admin_dashboard, name='admin_dashboard'),

        path('customer/dashboard/', customer_dashboard, name='customer_dashboard'),

        path('customer/register/', customer_register, name='customer_register'),




    

]