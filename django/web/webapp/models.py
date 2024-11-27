from django.db import models

class Contact(models.Model):
    name = models.TextField(max_length=50)
    username = models.TextField(max_length=80)
    password = models.TextField(max_length=50)
    date = models.DateField(auto_now=True)
    
    
    
    
    
