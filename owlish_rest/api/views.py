# Create your views here.

from rest_framework.decorators import api_view
from rest_framework import status # http result codes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from . import serializers


# Models
from customers.models import Customer

import pdb


"""@api_view(['GET'])
def Customers(request,pk = -1):
    
    #serializer_class=serializers.CustomerModelSerializer
    # If not looking for a specific customer
    if pk == -1:
        list = []

        for c in Customer.objects.all():
            list.append({
                'pk':c.pk,
                'first_name':c.first_name,
                'last_name':c.last_name,
                'email':c.email,
                'gender':c.gender,
                'company':c.company,
                'city':c.city,
                'title':c.title,
                'coord':c.coord,
            })
        
        return Response({
            'result':'ok',
            'customers':list
        })
    
    #if looking for a specific customer (pk is included in the req.)
    else:
        try:
            c = Customer.objects.get(pk=pk)
            #pdb.set_trace()
            return Response({
                'result':'ok',
                'customer':{
                    'pk':c.pk,
                    'first_name':c.first_name,
                    'last_name':c.last_name,
                    'email':c.email,
                    'gender':c.gender,
                    'company':c.company,
                    'city':c.city,
                    'title':c.title,
                    'coord':c.coord,
                }
            })
        except Exception as ex:
            return Response({
                "result" : 'failed',
                "reason" : str(ex),
                "status":status.HTTP_400_BAD_REQUEST
            })

"""

from rest_framework.views import APIView



class CustomersView(APIView):
    serializer_class = serializers.CustomerSerializer
    
    parameters =[
        openapi.Parameter('pk',in_=openapi.IN_QUERY,description='Primary key (identifier) of the customer',type=openapi.TYPE_INTEGER),
        openapi.Parameter('first_name',in_=openapi.IN_QUERY,description='Customer\'s first name',type=openapi.TYPE_STRING),
        openapi.Parameter('last_name',in_=openapi.IN_QUERY,description='Customer\'s last name',type=openapi.TYPE_STRING),
        openapi.Parameter('email',in_=openapi.IN_QUERY,description='Customer\'s email address',type=openapi.TYPE_STRING),
        openapi.Parameter('gender',in_=openapi.IN_QUERY,description='Customer\'s gender ("Male" or "Female")',type=openapi.TYPE_STRING),
        openapi.Parameter('company',in_=openapi.IN_QUERY,description='Customer\'s work company',type=openapi.TYPE_STRING),
        openapi.Parameter('city',in_=openapi.IN_QUERY,description='Customer\'s city address',type=openapi.TYPE_STRING),
        openapi.Parameter('title',in_=openapi.IN_QUERY,description='Customer\'s work position',type=openapi.TYPE_STRING),
        openapi.Parameter('coord',in_=openapi.IN_QUERY,description='Customer\'s coordinates',type=openapi.TYPE_STRING),

    ]
    @swagger_auto_schema(manual_parameters=parameters)
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
                list.append({
                    'pk':c.pk,
                    'first_name':c.first_name,
                    'last_name':c.last_name,
                    'email':c.email,
                    'gender':c.gender,
                    'company':c.company,
                    'city':c.city,
                    'title':c.title,
                    'coord':c.coord,
                })
            return Response(list)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
        #if looking for a specific customer (pk is included in the req.)
        



class HelloAPIView(APIView):
    """ TEST API VIEW """
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview = [
            'test1','test2',2123
        ]

        return Response({
            'message':'ok',
            'an_apiview':an_apiview
        })

    def post(self, request):
        """create a msg with our name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello, {name}'
            return Response({
                'message':message
            })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self,request,pk=None):
        """Update an element"""
        return Response({
            'method':'PUT'
        })

    def patch(self,request,pk=None):
        """Partially Update an element"""
        return Response({
            'method':'PATCH'
        })
    
    def delete(self,request,pk=None):
        """delete an element"""
        return Response({
            'method':'DELETE'
        })
        
        
        