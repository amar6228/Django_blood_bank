"""bdonation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from blood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blood.urls')),
    # path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('need',views.need,name='need'),
    path('donate',views.donate,name='donate'),
    path('donateblood',views.donateblood,name='donateblood'),
    path('needblood',views.needblood,name='needblood'),
    
    path('facts',views.facts,name='facts'),
    path('searchbloodbanks',views.searchbloodbanks,name='searchbloodbanks'),
    path('searchbloodcamps',views.searchbloodcamps,name='searchbloodcamps'),
    path('requestlist',views.requestlist,name='requestlist'),
    path('donorlist',views.donorlist,name='donorlist'),
    path('citydonar',views.citydonar,name='citydonar'),
    path('nearestpatient',views.nearestpatient,name='nearestpatient'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('donationmanual',views.donationmanual,name='donationmanual'),
    path('donorfitnesschart',views.donorfitnesschart,name='donorfitnesschart'),
]
