from django.shortcuts import render


from django.http import HttpResponse
from django.template import loader
from ansible.module_utils.gitlab import request

from clients.form import buyer, seller
from django.http.request import HttpRequest

def homepage(request):
    return HttpResponse("<h1>DONE FORM3 !! First Page<h1>")

def hello(request):
    return  HttpResponse("<h2>Hello, welcome to django<h2>")

def temp(request):
    temp1 = loader.get_template('home.html')
    
    name = {
        'myName': 'Khanh'
        }
    
    return HttpResponse(temp1.render(name))


def fom1(request):
    form1 = buyer()
    return render(request, "home.html", {"fom1": form1})

def fom2(request):
    form2 = seller
    return render(request, "home.html", {"fom2": form2, 'att': form2})



