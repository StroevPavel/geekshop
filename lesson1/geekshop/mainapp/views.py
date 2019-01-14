from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def main(request):
    return render(request, 'mainapp/index.html')


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
