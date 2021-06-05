from django.http.response import HttpResponse
import csv
from clients.users import Users
from reportlab.pdfgen import canvas


def getCSV(request):
    resp = HttpResponse(content_type='text/csv')
    
    resp['Content-Disposition'] = 'attachment; filename = "django.csv" '
    
    writer = csv.writer(resp)
    writer.writerow(['1001', 'John', 'Domil', 'CA'])
    writer.writerow(['1002', 'Amit', 'Mukhaji', 'LA', ' "TESTing" '])
    
    return resp


def getDatabase(request):
    
    resp = HttpResponse(content_type = 'text/csv')
    resp['Content-Disposition'] = 'attachment; filename="db.csv"'
    
    clients = Users.objects.all()
    writer = csv.writer(resp)
    
    for c in clients:
        writer.writerow([c.id, c.firstname, c.lastname, c.email, c.image])
        
    return resp

def getPDF(request):
    resp = HttpResponse(content_type = 'application/pdf')
    resp['Content-Disposition'] = 'attachment; filename="file.pdf"'
    
    p = canvas.Canvas(resp)
    p.setFont('Times-Roman', 25)
    p.drawString(100, 700, 'Hello This is PDF Django')
    p.showPage()
    p.save()
    
    return resp
    
    
    
    
    


        
    
    