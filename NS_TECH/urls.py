"""NS_TECH URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from .views import homepage, certificatefind,subadmin, contact_us,subadminpermissions, adminlogin, adminpage, admission, adminedit,ourservices, certificatecourses, diplomacourses, languagecourses, changepassword

urlpatterns = [
    path('', homepage, name='home'),
    path('verification', certificatefind, name='verification'),
    path('admissionform',admission,name="admission"),
    path('searchresult', certificatefind, name='searchresult'),
    path('contactus', contact_us, name='contact_us' ),
    path('admin', adminlogin, name='admin'),
    path('admin/kashif', adminpage, name='adminpage'),
    path('admin/kashif/edit', adminedit, name='adminedit'),
    path('services', ourservices, name='ourservices'),
    path('certficate-courses', certificatecourses, name='certificatecourses'),
    path('diploma-courses', diplomacourses, name='diplomacourses'),
    path('language-courses', languagecourses, name='languagecourses'),
    path('permissions', subadminpermissions, name='subadminpermissions'),
    path('subadmin', subadmin, name='subadmin'),
    path('changepassword', changepassword, name='changepassword')
]
