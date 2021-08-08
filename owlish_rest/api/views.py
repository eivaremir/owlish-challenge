#from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """ TEST API VIEW """

    def get(self,request,format=None):
        an_apiview = [
            'test1','test2',2123
        ]

        return Response({
            'message':'ok',
            'an_apiview':an_apiview
        })