from django.shortcuts import render
from rest_framework import generics
from API.models import AppDetails
from API.serializers import AppDetailSerializers

def home(request):
    return render(request, "index.html")

class  AppList(generics.ListCreateAPIView):
    queryset = AppDetails.objects.all()
    serializer_class = AppDetailSerializers

class Appinfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppDetails.objects.all()  
    serializer_class = AppDetailSerializers