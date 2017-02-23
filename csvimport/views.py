from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .utils import *
from .models import CI, CIDataValue


def index(request):
    return render(request, 'csvimport/index.html', {})



