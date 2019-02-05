from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user).order_by('product__category')
    else:
        return []

@login_required
def basket(request):
    content = {
        'basket': get_basket(request.user)
    }
    return render(request, 'basketapp/basket.html', content)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('unit', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return render(request, 'basketapp/basket.html', content)
