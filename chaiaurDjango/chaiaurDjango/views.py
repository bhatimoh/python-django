from django.http import HttpResponse
from django.shortcuts import render
def home(request):
  # return HttpResponse("hello this is my home page")
  return render(request,'index.html')

def about(request):
  return HttpResponse("hello this is my about page")

def contact(request):
  return HttpResponse("hello this is my contact page")


