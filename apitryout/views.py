from django.shortcuts import render
from rest_framework.decorators import APIView
from .models import test
from .serializers import testserializer
from rest_framework.response import Response

# Create your views here.
class showall(APIView):
    def get(self,request):
        profiles=test.objects.all()
        allprofiles=testserializer(profiles,many=True)
        return Response(allprofiles.data)

    def post(self,request):
        allprofiles=testserializer(data=request.data)
        if allprofiles.is_valid():
            allprofiles.save()
            return Response(allprofiles.data)
        else:
            return Response('Data is Invalid')

class showselected(APIView):
    def get(self,request,key):
        profiles=test.objects.get(id=key)
        selectedprofs=testserializer(profiles)
        return Response(selectedprofs.data)

    def delete(self,request,key):
        profiles=test.objects.get(id=key)
        profiles.delete()
        return Response("Deletion completed!!!")
    
    def put(self,request,key):
        profiles=test.objects.get(id=key)
        selectedprofs=testserializer(profiles,request.data)
        if selectedprofs.is_valid():
            selectedprofs.save()
            return Response(selectedprofs.data)
        else:
            return Response("Invalid data")
