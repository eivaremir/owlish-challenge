#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status # http result codes

from . import serializers

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