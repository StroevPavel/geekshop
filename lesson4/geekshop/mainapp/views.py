from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
	return render(request, 'mainapp/index.html')


def catalog(request, catnum=None):
	products = Product.objects.all() #[:4]
	content = {'products': products}
	print(catnum)
	return render(request, 'mainapp/catalog.html', content)

def contacts(request):
	return render(request, 'mainapp/contacts.html')

def goods(request):
	return render(request, 'mainapp/good_1.html')

def base(request):
	return render(request, 'mainapp/base.html')