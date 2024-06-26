from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def lasya(request):
    return HttpResponse('<h1><marquee>How are you??</marquee></h1>')


def shree(request):
    return render(request,'shree.html')