"""testDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from clients.allviews import views, view2, view3, view4, view5

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('temp/', views.temp),
    path('form1/', views.fom1),
    path('form2/', views.fom2),
    path('form3/', view2.validatedForm),
    path('form3bt/', view2.byBootstrap),
    path('form3/details1', view2.getDetails1),
    path('form3/details2', view2.getDetails2),
    path('setsession/', view3.setSession),
    path('getsession/', view3.getSessionData),
    path('setcookie/', view4.setCookie),
    path('getcookie/', view4.getCookie),
    path('getcsv/', view5.getCSV),
    path('getdatabase/', view5.getDatabase),
    path('getpdf/', view5.getPDF),
    
]
