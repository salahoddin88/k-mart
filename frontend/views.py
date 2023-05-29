from django.shortcuts import render
from cms.models import Slider
from product.models import ProductCategory, Product, ProductTag


def home_page(request):
    """ Home page of k-mart E-com  """
    sliders = Slider.objects.filter(status=True)
    product_categories = ProductCategory.objects.filter(status=True)[0:3]
    fashion_products = Product.objects.filter(status=True)[0:5]
    product_tags = ProductTag.objects.filter(status=True)[0:2]
    context = {
        'slider' : sliders,
        'product_categories' : product_categories,
        'fashion_products' : fashion_products,
        'product_tags' : product_tags
    }
    return render(request, 'home.html', context)
