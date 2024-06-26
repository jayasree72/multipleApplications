from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Vrindha(request):
    return HttpResponse('<h1>Vrindha is good girl</h1>')


def Vandhana(request):
    return render(request,'vandhana.html')