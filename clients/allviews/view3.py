from django.http.response import HttpResponse
from django.template.defaulttags import csrf_token
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.shortcuts import redirect



def setSession(request):
    request.session['sPhone'] = '0703601738'
    request.session['sAddress'] = 'D7, HCM city'
    
    #HTTP_REFERER ONLY EXIST AS MOVING BY PROGRAM NOT DIRECTLY FROM ADDRESS BAR
    try:
        print(request.META['HTTP_REFERER'])
    except:
        pass
    
    return HttpResponse('<li>Session is setted </li>' + 
                '<li><a href="http://127.0.0.1:8000/getsession" >MOVE TO GETSESSION</a></li>')

def getSessionData(request):
    
    # FROM VIEW2 IN VALIDATEDFORM
    # MUST RUN /FORM3 FIRST
    try:
        firstname = request.session['sFirstName']
        email = request.session['sEmail']
        
    except:
        return redirect('/form3/')
    
    # MUST RUN SETSESSION FIRST
    try:
        phone = request.session['sPhone']
        address = request.session['sAddress']
    except:
        return redirect('/setsession/')
    
    return HttpResponse(
        '<li>name:   '+ firstname + '</li>' +
        '<li>email:  '+ email + '</li>' +
        '<li>mobile: '+ phone + '</li>' +
        '<li>at      '+ address + '</li>' 
        ) 