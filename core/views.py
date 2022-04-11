from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Product

@login_required
def cart(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'core/cart.html', context)