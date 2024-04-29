from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from rest_framework import generics
from services.models import Service
from services import serializer
def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/index.html')


def name(request: HttpRequest):
    return render(request, "pages/info/name.html")


def project(request: HttpRequest):
    return render(request, "pages/info/project.html")

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = serializer.ServiceSerializer

class ServiceList2(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = serializer.ServiceSerializer