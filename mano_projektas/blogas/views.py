from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pagrindinis(request):
    return HttpResponse("Sveiki atvykę į pagrindinį puslapį!")