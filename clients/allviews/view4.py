from django.http.response import HttpResponse
from django.http import response

def setCookie(request):
    
    resp = HttpResponse("Cookie setted")
    
    resp.set_cookie('userName', request.META['LOGNAME'])
    resp.set_cookie('email', request.META['EMAIL_USER'])
    
    print(resp)
    
    return resp
    
def getCookie(request):
    
    name = request.COOKIES['userName']
    email = request.COOKIES['email']
    
    print(request)
    
    return HttpResponse(
        '<li>' + name + '</li>' +
        '<li>' + email + '</li>' 
        
        )
    