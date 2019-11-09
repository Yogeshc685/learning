from django.shortcuts import render
from .models import Cart
# Create your views here.

def cart(request):
    cart=Cart.objects.all()[0]
    context={"cart":cart}
    template="cart.html"
    return render(request,template,context)


def update_cart(request,slug):
    pass
