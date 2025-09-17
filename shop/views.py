from django.shortcuts import get_object_or_404, render

from .models import Product


def product_list(request):
    return render(request, "shop/list.html", {"products": Product.objects.all()})


def product_detail(request, sku):
    product = get_object_or_404(Product, sku=sku)
    return render(request, "shop/detail.html", {"product": product})
