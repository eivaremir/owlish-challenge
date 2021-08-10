
from django.core.exceptions import ValidationError
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
    lat = serializers.FloatField(required=False)
    lng = serializers.FloatField(required=False)
    class Meta:
        model = Customer
        fields =('pk','first_name','last_name','email','gender','company','city','title','lat','lng')


class PatchCustomerSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=True)
    first_name= serializers.CharField(max_length=255,required=False)
    last_name=serializers.CharField(max_length=255,required=False)
    email= serializers.EmailField(max_length=255,required=False)
    gender=serializers.CharField(max_length=6,required=False)
    company=serializers.CharField(max_length=255,required=False)
    city=serializers.CharField(max_length=255,required=False)
    title=serializers.CharField(max_length=255,required=False)
    def validate(self, data):
        customer_to_be_updated = Customer.objects.filter(pk=data.get('pk',0))
        customer_by_email =  Customer.objects.filter(email=data.get('email',''))
        #import pdb; pdb.set_trace()

        if len(Customer.objects.filter(pk=data.get('pk',0))) == 0 :
            raise ValidationError("client does not exist")
        # if customer got by email is different from client to be updated (arent the same)
        if len(customer_by_email) > 0 and customer_by_email[0].pk !=customer_to_be_updated[0].pk :
            raise ValidationError("Email already in use")
        return data
    class Meta:
        model = Customer
        fields =('pk','first_name','last_name','email','gender','company','city','title')


class DeleteCustomerSerializer(serializers.ModelSerializer):
    
    pk = serializers.IntegerField(required=True)
    def validate(self, data):
        
        if len(Customer.objects.filter(pk=data.get('pk',0))) == 0 :
            raise ValidationError("client does not exist")

        
        return data
    class Meta:
        model = Customer
        fields =('pk',)
    

    
class CustomerSerializer(serializers.Serializer):
    first_name= serializers.CharField(max_length=255)
    last_name=serializers.CharField(max_length=255)
    email= serializers.EmailField(max_length=255)
    gender=serializers.CharField(max_length=6,required=False)
    company=serializers.CharField(max_length=255,required=False)
    city=serializers.CharField(max_length=255,required=True)
    title=serializers.CharField(max_length=255,required=False)
    

    lat = serializers.FloatField(required=False)
    lng = serializers.FloatField(required=False)

    class Meta:
        model = Customer
        fields =('first_name','last_name','email','gender','company','city','title','lat','lng')
        
    def validate(self, data):
        if len(Customer.objects.filter(email=data.get('email',''))) > 0:
            raise ValidationError("Email Exists")
        return data

    #def create(self,validated_data):
        # get customer coordinates
        
    #    return Customer(**validated_data)
    
