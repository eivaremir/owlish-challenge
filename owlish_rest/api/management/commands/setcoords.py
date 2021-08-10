from django.core.management.base import BaseCommand
from customers.models import Customer


class Command(BaseCommand):
    help = 'Display'
        
    def handle(self,*args,**kwargs):
        for c in Customer.objects.all():
            self.stdout.write(f"setting coordinates for {c.first_name} {c.last_name}")        
            c.set_coordinates()
            c.save()
            self.stdout.write(f"coordinates for {c.first_name} {c.last_name} are {c.lat},{c.lng}")  
        self.stdout.write("finished setting coordinates")        
        #import pdb; pdb.set_trace()
        
