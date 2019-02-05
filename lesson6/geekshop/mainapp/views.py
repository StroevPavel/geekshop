from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render
from .models import ProductCategory, Product
from basketapp.models import Basket

def get_basket(user):
	if user.is_authenticated:
		return Basket.objects.filter(user=user)
	else:
		return []

def main(request):
	content = {
		'basket': get_basket(request.user)
	}

	return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None):

	title = 'Products'

	# меню категорий
	links_menu = ProductCategory.objects.all()

	# вывод товаров
	#products = Product.objects.all() #[:4] # old
	if pk is not None:
		if pk == 0:
			products = Product.objects.all().order_by('price')
			category = {'name': 'все'}
			title = 'Products - All'
		else:
			category = get_object_or_404(ProductCategory, pk=pk)
			products = Product.objects.filter(category__pk=pk).order_by('price')
			title = 'Products - ' + category.name
			print(title)

		content = {
			'title': title,
			'links_menu': links_menu,
			'category': category,
			'products': products,
			'basket': get_basket(request.user)
		}

		return render(request, 'mainapp/catalog.html', content)

	same_products = Product.objects.all()[:4]

	content = {
		'title': title, 
		'links_menu': links_menu, 
		'products': same_products,
		'basket': get_basket(request.user)
	}

	# content = {'products': products} # old

	return render(request, 'mainapp/catalog.html', content)

def contacts(request):
	content = {
		'basket': get_basket(request.user)
	}

	return render(request, 'mainapp/contacts.html', content)

def unit(request, pk=None):
	content = {
		'product': get_object_or_404(Product, pk=pk), 
		'basket': get_basket(request.user)
	}

	return render(request, 'mainapp/unit.html', content)

def base(request):
	return render(request, 'mainapp/base.html')