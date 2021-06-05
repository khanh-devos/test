
from clients.users import Users
from ansible.module_utils.gitlab import request
from clients.form import buyer
from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from clients.function.func1 import handle_uploaded_file
from django.http.request import HttpRequest


def validatedForm(request):
    if request.method == "POST":
        form3 = buyer(request.POST, request.FILES)
        
        if form3.is_valid():   #INPUTTED
            handle_uploaded_file(request.FILES['image'])
            
            #for SESSION IN VIEW3
            request.session['sFirstName'] = request.POST['firstname']
            request.session['sEmail'] = request.POST['email']
            
            
            return redirect("/form3/details1")   #CHANGE TO /DETAILS2 FOR httpRESPONSE   

    else:
        form3 = buyer
        
    return render(request, "home.html", {"fom3": form3}) 

def byBootstrap(request):
    if request.method == "POST":
        form3 = buyer(request.POST, request.FILES)
        
        if form3.is_valid():   #INPUTTED
            handle_uploaded_file(request.FILES['image'])
            
            #for SESSION IN VIEW3
            request.session['sFirstName'] = request.POST['firstname']
            request.session['sEmail'] = request.POST['email']
            
            
            return redirect("/form3/details1")   #CHANGE TO /DETAILS2 FOR httpRESPONSE   

    else:
        form3 = buyer
        
    return render(request, "bootstrap.html", {"fom3": form3})

    
def getDetails1(request):
    
    try: 
        pre_url = request.META['HTTP_REFERER']
    except:
        pre_url = 'ONLY ENTER THIS SIDE AFTER INPUT AT URL: /FORM3, OTHERWISE CANNOT SEE PREVIOUS URL'
    
    DT = {
        'host': request.get_host(),
        'path': request.get_full_path(),
        'method': request.method,
        'upfiles': request.FILES,
        'content_type': request.content_type,
        'headers: PREVIOUS_URL ?? ': pre_url,
        'absolute_uri' : request.build_absolute_uri,
        }
    
    print(pre_url)

    return render(request, "home.html", {"DT": DT})
    
    
def getDetails2(request):
    
    response = {
        'content': HttpResponse.content,
        'charset': HttpResponse.charset,
        'streaming': HttpResponse.streaming,
        }
    
    return render(request, "home.html", {'response': response})






    