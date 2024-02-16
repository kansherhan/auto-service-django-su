from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'pages/index.html')


def name(request: HttpRequest):
    return render(request, "pages/info/name.html")


def project(request: HttpRequest):
    return render(request, "pages/info/project.html")
