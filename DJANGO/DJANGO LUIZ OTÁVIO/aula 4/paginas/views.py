from django.shortcuts import render


def index(request):
    return render(request, 'armazena/index.html')


def sobre(request):
    return render(request, 'armazena/sobre.html')

# Create your views here.
