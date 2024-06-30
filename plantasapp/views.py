from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request, 'plantasapp/index.html')

def tierra(request):
    context={}
    return render(request, 'plantasapp/tierra.html', context)

def macetero(request):
    context={}
    return render(request, 'plantasapp/macetero.html', context)

def flores(request):
    context={}
    return render(request, 'plantasapp/flores.html', context)

def arbustos(request):
    context={}
    return render(request, 'plantasapp/arbustos.html', context)