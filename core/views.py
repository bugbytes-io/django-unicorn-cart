from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def cart(request):
    context = {}
    return render(request, 'core/cart.html', context)