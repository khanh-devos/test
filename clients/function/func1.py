

def handle_uploaded_file(f):
    with open('/home/khanh/MORE/Python/testDjango/clients/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)