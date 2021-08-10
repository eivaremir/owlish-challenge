from django.db import models
#from django.contrib.auth.models import User
# Create your models here.
import os
import requests
import urllib
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
    lat = models.FloatField(blank=True,null=True)
    lng = models.FloatField(blank=True,null=True)
    maps_link = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return (self.first_name if self.first_name else '' )+\
                " "+(self.last_name if self.last_name else '')+\
                f'<{self.email}>'
    
    
    @classmethod
    def get_coordinates(cls,address):
        key = os.environ['GEOCODEAPIKEY']
        address = urllib.parse.quote(address)
        geocode_response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={key}').json()
        return geocode_response['results'][0]['geometry']['location']
    
    @classmethod
    def get_maps_link(cls,address):
        coords = Customer.get_coordinates(address)
        lat, lng = (coords['lat'], coords['lng'])
        return f'https://www.google.com/maps/search/{lat},{lng}'

    def coordinates(self):
        return self.get_coordinates(self.city)


from django.db.models.signals import pre_save, pre_init,post_init


def set_customer_coordinates(sender, instance,**kwargs):
    """Function to be executed just after customer creation to setup the coordinates"""
    if instance.city:
        instance.lat, instance.lng = list(map(lambda x:float(x), Customer.get_maps_link(instance.city).split('/')[-1].split(',')))
        instance.maps_link = f'https://www.google.com/maps/search/{instance.lat},{instance.lng}'
    
def update_customer_coordinates(sender, instance, **kwargs):
    """Function to be executed just after customer UPDATES """

     # setup the new coordinates
     # test first, can cause KeyError Exception afterwards
    if kwargs['update_fields'] :
        # if city has content and city is within the updated fields
        if len(instance.city)>0 and 'city' in kwargs['update_fields'] :
            # get coordinates
            instance.lat, instance.lng = list(map(lambda x:float(x), Customer.get_maps_link(instance.city).split('/')[-1].split(',')))
            instance.maps_link = f'https://www.google.com/maps/search/{instance.lat},{instance.lng}'
        # if city has been deleted
        elif len(instance.city)==0 and 'city' in kwargs['update_fields']:
            instance.lat, instance.lng = (None,None)
            instance.maps_link = None
    

pre_save.connect(update_customer_coordinates, sender=Customer)
post_init.connect(set_customer_coordinates, sender=Customer)