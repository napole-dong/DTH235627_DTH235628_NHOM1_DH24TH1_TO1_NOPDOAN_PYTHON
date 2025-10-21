
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, welcome to the school app!")   
# Create your views here.
