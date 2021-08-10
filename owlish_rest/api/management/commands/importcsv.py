from django.core.management.base import BaseCommand
from customers.models import Customer
import csv 

class Command(BaseCommand):
    help = 'Display'
    def add_arguments(self, parser) -> None:
        parser.add_argument('file',type=str,help="filename")
        
    def handle(self,*args,**kwargs):
        f = open(kwargs['file']) 

        self.stdout.write(f"opening file {kwargs['file']}") 
        reader = csv.reader(f, delimiter=',', quotechar='"')  
        
        header = next(reader)
        self.stdout.write("importing") 
        for row in reader: 
            try:
                Customer.objects.create(
                    first_name = row[1],
                    last_name = row[2],
                    email = row[3],
                    gender = row[4],
                    company = row[5],
                    city = row[6],
                    title = row[7]
                )
            except Exception as ex:
                self.stdout.write(str(ex))
        self.stdout.write("finished import")        
        #import pdb; pdb.set_trace()
        
