from django.shortcuts import render
from django.http import HttpResponse

def one(request):
    return HttpResponse("Hello One")

def two(request):
    return HttpResponse("Hello Two")

def three(request):
    return HttpResponse("Hello Three")
