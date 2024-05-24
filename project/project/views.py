from django.http import HttpResponse as hr;
from django.shortcuts import render

def home(request):
  return render(request,'index.html')

def about(request):
  return hr("about page")

def contact(request):
  return hr("contact page is here")