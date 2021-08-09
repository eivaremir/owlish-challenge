from django.db import models
#from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    '''
    Customer Model
    '''
    
    first_name= models.CharField(max_length=255,blank=True,null=True)
    last_name=models.CharField(max_length=255,blank=True,null=True)
    email= models.EmailField(max_length=255,unique=True)
    gender=models.CharField(max_length=6,blank=True,null=True)
    company=models.CharField(max_length=255,blank=True,null=True)
    city=models.CharField(max_length=255,blank=True,null=True)
    title=models.CharField(max_length=255,blank=True,null=True)
    coord = models.CharField(max_length=255,blank=True,null=True)
    
    def __str__(self):
        return (self.first_name if self.first_name else '' )+\
                " "+self.last_name if self.last_name else ''+\
                f'<{self.email}>'