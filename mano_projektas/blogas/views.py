from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def pagrindinis(request):
#     return HttpResponse("Sveiki atvykę į pagrindinį puslapį!")

def pagrindinis(request):
    context = {
        "pavadinimas": "Mano puslapis",
        'antraste': "Sveiki atvykę!",
    }
    return render(request, template_name="pagrindinis.html", context=context)

def apie(request):
    context = {
        "tekstas": "Čia yra mano svetainė, kurioje demonstruoju, kaip veikia Django viewsai ir šablonai.",
        "pavadinimas": "apie",
    }
    return render(request, template_name='apie.html', context=context)