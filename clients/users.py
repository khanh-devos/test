from __future__ import unicode_literals

from django.db import models



class Users(models.Model):

    
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    
    email= models.EmailField()
    image = models.FileField()  #FOR UPLOAD 
    
    class Meta:
        db_table = "clientsInfo"
        