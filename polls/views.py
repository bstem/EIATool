from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, user. You're at the polls index.")
