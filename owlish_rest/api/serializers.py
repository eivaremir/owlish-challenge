from rest_framework import serializers
from customers.models import Customer

class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    

class GetCustomerSerializer(serializers.ModelSerializer):
    
    pk = serializers.IntegerField(required=False)
    first_name= serializers.CharField(max_length=255,required=False)
    last_name=serializers.CharField(max_length=255,required=False)
    email= serializers.EmailField(max_length=255,required=False)
    gender=serializers.CharField(max_length=6,required=False)
    company=serializers.CharField(max_length=255,required=False)
    city=serializers.CharField(max_length=255,required=False)
    title=serializers.CharField(max_length=255,required=False)
    coord = serializers.CharField(max_length=255,required=False)
    class Meta:
        model = Customer
        fields =['pk','first_name','last_name','email','gender','company','city','title','coord']
    

    
class CustomerSerializer(serializers.Serializer):
    first_name= serializers.CharField(max_length=255)
    last_name=serializers.CharField(max_length=255)
    email= serializers.EmailField(max_length=255)
    gender=serializers.CharField(max_length=6)
    company=serializers.CharField(max_length=255)
    city=serializers.CharField(max_length=255)
    title=serializers.CharField(max_length=255)
    coord = serializers.CharField(max_length=255)
    
