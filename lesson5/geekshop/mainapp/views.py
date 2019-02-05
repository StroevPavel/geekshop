from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render
from .models import ProductCategory, Product
from basketapp.models import Basket

def main(request):
	return render(request, 'mainapp/index.html')


def catalog(request, pk=None):
	print(pk)

	title = 'Products'

	# корзина
	basket = []
	if request.user.is_authenticated:
		basket = Basket.objects.filter(user=request.user)

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
			'basket': basket
		}

		return render(request, 'mainapp/catalog.html', content)

	same_products = Product.objects.all()[:4]

	content = {
		'title': title, 
		'links_menu': links_menu, 
		'products': same_products,
		'basket': basket
	}

	# content = {'products': products} # old

	return render(request, 'mainapp/catalog.html', content)

def contacts(request):
	return render(request, 'mainapp/contacts.html')

def goods(request):
	return render(request, 'mainapp/good_1.html')

def base(request):
	return render(request, 'mainapp/base.html')