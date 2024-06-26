from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def yash(request):
    return HttpResponse('<h1><marquee>What about you yash</marquee></h1>')


def Akarsh(request):
    return render(request,'Akarsh.html')