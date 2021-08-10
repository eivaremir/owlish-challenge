# Create your views here.

#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status # http result codes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#debugging
import pdb


from . import serializers

# Models
from customers.models import Customer


class CustomersView(APIView):
    serializer_class = serializers.CustomerSerializer
    
    get_parameters =[
        openapi.Parameter('pk',in_=openapi.IN_QUERY,description='Primary key (identifier) of the customer',type=openapi.TYPE_INTEGER),
        openapi.Parameter('first_name',in_=openapi.IN_QUERY,description='Customer\'s first name',type=openapi.TYPE_STRING),
        openapi.Parameter('last_name',in_=openapi.IN_QUERY,description='Customer\'s last name',type=openapi.TYPE_STRING),
        openapi.Parameter('email',in_=openapi.IN_QUERY,description='Customer\'s email address',type=openapi.TYPE_STRING),
        openapi.Parameter('gender',in_=openapi.IN_QUERY,description='Customer\'s gender ("Male" or "Female")',type=openapi.TYPE_STRING),
        openapi.Parameter('company',in_=openapi.IN_QUERY,description='Customer\'s work company',type=openapi.TYPE_STRING),
        openapi.Parameter('city',in_=openapi.IN_QUERY,description='Customer\'s city address',type=openapi.TYPE_STRING),
        openapi.Parameter('title',in_=openapi.IN_QUERY,description='Customer\'s work position',type=openapi.TYPE_STRING),
        openapi.Parameter('lat',in_=openapi.IN_QUERY,description='Customer\'s latitude coordinate',type=openapi.TYPE_NUMBER),
        openapi.Parameter('lng',in_=openapi.IN_QUERY,description='Customer\'s longitude coordinate',type=openapi.TYPE_NUMBER),

    ]
    @swagger_auto_schema(manual_parameters=get_parameters)
    def get(self,request):
        serializer = serializers.GetCustomerSerializer(data = request.GET)

        #valid_fields = []
        query ={}
        for a in request.GET : 
            for b in Customer._meta.get_fields(): 
                if a ==b.name:
                    #valid_fields.append(a)
                    query[a+"__contains"]=request.GET.get(a)
                    #print (a,'=',b.name,' -> ',a ==b.name)
        if request.GET.get('pk'):
            query["pk"]=request.GET.get('pk')
        print(query)
        #pdb.set_trace()
        
        if serializer.is_valid():
            list = []
            if len(query.items()) > 0:
                result = Customer.objects.filter(**query)
                    
            else:
                result = Customer.objects.all()   
            for c in result:
                #revisar metodo optimizado https://www.geeksforgeeks.org/how-to-convert-models-data-into-json-in-django/
                list.append({
                    'pk':c.pk,
                    'first_name':c.first_name,
                    'last_name':c.last_name,
                    'email':c.email,
                    'gender':c.gender,
                    'company':c.company,
                    'city':c.city,
                    'title':c.title,
                    'lat':c.lat,
                    'lng':c.lng,
                    'maps_link':c.maps_link
                })
            return Response(list)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['first_name','last_name','email'],
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING,description="Customer's first name",title="First Name"),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING,description="Customer's last name",title="Last Name"),
                'email': openapi.Schema(type=openapi.TYPE_STRING,description="Customer's email address",title="E-mail"),
                'gender': openapi.Schema(type=openapi.TYPE_STRING,description="Customer's biological gender",title="Gender"),
                'city': openapi.Schema(type=openapi.TYPE_STRING,description="Customer's Address",title="City address"),
                #'last_name': openapi.Schema(type=openapi.TYPE_STRING,description="Customer's last name",title="Last Name"),
            },
        ))
    def post(self,request):
        """Creates a new customer"""
        
        serializer = self.serializer_class(data =request.data)
       
        if serializer.is_valid():
            #customer = serializer.create(serializer.validated_data)
            
            pdb.set_trace()
            customer=Customer.objects.create(**serializer.validated_data)
            #if  'city' in serializer.validated_data:
            
            customer.save()
            #else: 
            #    customer.save()

            return Response({
                    "status":"ok",
                    "customer":serializer.validated_data
                },
                status.HTTP_201_CREATED
            )
        else:
            #pdb.set_trace()
            return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST     )

